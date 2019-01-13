# Author: Kiet Tran
# Init date: 12/21/2018
# Work in progress

from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import sys, time, random, datetime
import os.path
import serial_asyncio
import serial
import numpy        as np
import pyqtgraph    as pg
from   pyqtgraph    import PlotWidget
from   collections  import deque
from   functools    import partial # passing args into slot functions

from main_UI import Ui_MainWindow as uiwindow # Import the Python script exported from Qt Creator .ui file

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.refreshRate    = 10        # default sampling interval
        self.setSpeed       = 50        # default pulling speed
        self.upperSpeedLim  = 55        # Upper pulling speed
        self.lowerSpeedLim  = 20        # Lower pulling speed
        self.speedStepSize  = 1         # default increment/decrement step size for increase/decreasing pulling speed
        self.isRunning      = False     # True when motor is rotating, else False
        self.logDir         = None      # String to store the directory for writing log file
        self.data           = deque()   # Queue to store speed data
        self.doneWriting    = False     # Flag to indicate whether log data was written or not
        
        '''Setup timer to polling sample at regular interval'''
        self.time   = QTime()
        self.time.start()

        self.timer  = QTimer()

        self.ui = uiwindow()
        self.ui.setupUi(self)

        '''setup signal and slots'''
        self.ui.incrementBtn.clicked.connect(self.incrementSpeed)
        self.ui.decrementBtn.clicked.connect(self.decrementSpeed)
        self.ui.startBtn.clicked.connect(   self.startTest)
        self.ui.stopBtn.clicked.connect(    self.stopTest)        
        self.ui.toolButton.clicked.connect(partial(     self.logData, True))    # Data logging group
        self.ui.dataloggingGroup.toggled.connect(partial(self.logData, False))
        self.ui.manualDial.valueChanged.connect(        self.manual_control)    # Manual control dial
        
        '''configure velocity plot'''
        self.plotItem = self.ui.plotarea.getPlotItem()
        self.ui.plotarea.setAntialiasing(True)
        self.plotItem.enableAutoRange(axis="y", enable=True)
        self.plotItem.setXRange(min=0, max=5000, padding=0.1)
        self.plotItem.setLabel('left','Pulling speed [in/s]')
        self.plotItem.setLabel('bottom', 'Time [s]')
        self.plotItem.showAxis('right') # Show the plot box
        self.plotItem.showAxis('top')   # Show the plot box
        self.plotItem.setTitle('<span style="font-family:sans-serif">Pulling Speed over Time</span>')
        self.plotItem.showGrid(x=True, y=True, alpha=0.3)
        print("Plot title and axis labels updated")

    ''' SLOT FUNCTIONS '''
    def updatePlot(self):
        ''' Gets called periodically by a QtTimer to update the speed plot 
        in 5 seconds after hitting the start button'''
        self.data.append({'x': self.time.elapsed(), 'y': np.random.uniform(-1, 1)})
        x = [item['x'] for item in self.data]
        y = [item['y'] for item in self.data]
        (self.plotItem.listDataItems())[0].setData(x=x, y=y, pen= pg.mkPen('w', width=1, style=QtCore.Qt.DotLine))

        if self.time.elapsed() >= 5000: # only do logging for 5 seconds
            self.timer.stop() # Stop calling updatePlot periodically
            self.ui.startBtn.setEnabled(True)         
            
            #Write data to file
            if self.ui.dataloggingGroup.isChecked() and not self.doneWriting:
                if self.logDir is None: # check if the log directory string is empty
                    writePath = '/home/akiet00/Desktop/data_log_' + datetime.datetime.today().strftime('%Y%m%d_%I%M%S') + '.csv' # default directory
                else:
                    print("Writing log to custom path")
                    writePath = self.logDir + '/data_log_' + datetime.datetime.today().strftime('%Y%m%d_%I%M%S') + '.csv'
                
                with open(writePath,'w+') as file:
                    file.writelines('time [miliseconds], velocity [in/s] \n')
                    for item in self.data:
                        file.write(str(item['x']) + ',' + str(item['y']) + '\n')
                self.doneWriting = True
            self.data.clear() # removed all stored data in the queue 

    def startTest(self):
        ''' Gets called when start button is triggered by user'''

        # Start the clock to record time between data points
        self.time.start()
        self.plotItem.addItem(pg.PlotDataItem())

        # Reset the logging flag
        self.doneWriting = False

        self.ui.startBtn.setEnabled(False) # Avoid double clicking issue
        print("Test started")
        # TODO: Send commands to motor
        
        # Collect the RPM and plot linear velocity
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(20) #update every 20 miliseconds

    def stopTest(self):
        ''' Gets called when stop button is triggered by user'''

        # TODO: stop the motor

        print("Test stopped")

    def manual_control(self):
        ''' Gets called when the manual control dial is moved by user'''
        val = self.ui.manualDial.value()
        self.ui.currentpositionLabel.setText(str(val) + "%")
        print("manual control dial changed %i" %val)

    def incrementSpeed(self):
        ''' Gets called when increment button is triggered by user'''
        self.ui.decrementBtn.setEnabled(True)
        if self.setSpeed>= self.upperSpeedLim:
            self.ui.incrementBtn.setEnabled(False)
            print("Hit speed upper limit")
        else:
            self.ui.incrementBtn.setEnabled(True)
            self.setSpeed += self.speedStepSize
            self.ui.setpullspeedLabel.setText(str(self.setSpeed))
        print("Current set speed %i" %self.setSpeed)

    def decrementSpeed(self):
        self.ui.incrementBtn.setEnabled(True)
        if self.setSpeed<=self.lowerSpeedLim:
            self.ui.decrementBtn.setEnabled(False)
            print("Hit speed lower limit")
        else:
            self.ui.decrementBtn.setEnabled(True)
            self.setSpeed -= self.speedStepSize
            self.ui.setpullspeedLabel.setText(str(self.setSpeed))
        print("Current set speed %i" %self.setSpeed)

    def logData(self,toolFlag=False):
        ''' Gets called when user check/uncheck the log data group box'''
        # Prompt where to save the file
        if self.ui.dataloggingGroup.isChecked():
            if (self.ui.lineEdit.text() and toolFlag) or not self.ui.lineEdit.text():
                """ 
                Prompt user to select a directory EITHER when there's already an existing log directory 
                path but user clicks on the directory tool button OR when the current directory path is empty
                """
                self.logDir = str(QFileDialog.getExistingDirectory(parent=self, 
                                    caption="Select a folder to save log file"))
                self.ui.lineEdit.setText(self.logDir)
                print("Logging data to ... %s" %self.logDir)
        else:
            print('Data logging is disabled')

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
main()