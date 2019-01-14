# Author: Kiet Tran
# Init date: 12/21/2018
# Work in progress

from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import QTimer, QTime, QPointF, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import sys, time, types, random, datetime
import serial
import numpy        as np
import pyqtgraph    as pg
from   collections  import deque
from   functools    import partial # passing args into slot functions

from main_UI import Ui_MainWindow as uiwindow # Import the Python script exported from Qt Creator .ui file
from arduino_serial import SerialMonitor, SerialSender
# TODO:
# - Add serial communication and parsing data from serial
# - Add serial command functions

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
        self.plotItem.setXRange(min=0, max=3000, padding=0.1)
        self.plotItem.setLabel('left','Pulling speed [in/s]')
        self.plotItem.setLabel('bottom', 'Time [s]')
        self.plotItem.showAxis('right') # Show the plot box
        self.plotItem.showAxis('top')   # Show the plot box
        self.plotItem.setTitle('<span style="font-family:sans-serif">Pulling Speed over Time</span>')
        self.plotItem.showGrid(x=True, y=True, alpha=0.3)
        print("Plot title and axis labels updated")

        '''Show the set speed on the plot'''
        self.setSpeedLine = pg.InfiniteLine(angle=0 , pos=self.setSpeed, pen=pg.mkPen(color='r' , width=3, style=QtCore.Qt.SolidLine)) # Start button color: (0,108,177)
        self.plotItem.addItem(self.setSpeedLine)

    '''HELPER FUNCTIONS'''
    def clearPlot(self):
        self.data.clear()
    	
    ''' SLOT FUNCTIONS '''
    def updatePlot(self):
        ''' Gets called periodically by a QtTimer to update the speed plot 
        in 5 seconds after hitting the start button'''
        if not self.doneWriting:
            self.data.append({'x': self.time.elapsed(), 'y': np.random.uniform(self.setSpeed-10, self.setSpeed+10)})
            x = [item['x'] for item in self.data]
            y = [item['y'] for item in self.data]
            #(self.plotItem.listDataItems())[0].setData(x=x, y=y, marker='+',pen= pg.mkPen('w', width=1, style=QtCore.Qt.DotLine))
            (self.plotItem.listDataItems())[0].setData(x=x, y=y, symbol= 'o',pen= pg.mkPen('w', width=3), antialias=True, brush=None)
            
            if self.time.elapsed() >= 3000: # only do logging for 3 seconds
                self.timer.stop() # Stop calling updatePlot periodically
                self.ui.startBtn.setEnabled(True)         
                
                #Write data to file
                if self.ui.dataloggingGroup.isChecked():
                    print('default log dir ', self.logDir)
                    if self.logDir==None: # check if the log directory string is empty
                        writePath = '/home/akiet00/Desktop/data_log_' + datetime.datetime.today().strftime('%Y%m%d_%I%M%S') + '.csv' # default directory
                    else:
                        print("Writing log to custom path")
                        writePath = self.logDir + '/data_log_' + datetime.datetime.today().strftime('%Y%m%d_%I%M%S') + '.csv'
                    try:
	                    with open(writePath,'w+') as file:
	                        file.writelines('time [miliseconds], velocity [in/s] \n')
	                        for item in self.data:
	                            file.write(str(item['x']) + ',' + str(item['y']) + '\n')
                    except Exception as Error:
	                        msgBox = QMessageBox()
	                        msg = ''
	                        if isinstance(Error, PermissionError):
	                        	msg = "This program doesn't have permission to save a file in the specified folder. Consider choosing a different folder and try to run the test again.\n"
	                        elif isinstance(Error, IOError):
	                        	msg = 'IO Error.\n'
	                        else:
	                        	msg = 'Unpredictable error occured. Please consider redo the test to log data.\n'
	                        msgBox.critical(self, 'Error saving log file', msg + '\nError Message: \n' + str(Error))
                
                self.clearPlot() # removed all stored data in the queue
                self.doneWriting = True

    def startTest(self):
        ''' Gets called when start button is triggered by user'''

        # Start the clock to record time between data points
        self.time.start()
        #self.plotItem.addItem(pg.PlotDataItem())
        self.scatterPlot = pg.ScatterPlotItem()
        self.plotItem.addItem(self.scatterPlot)

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
        self.timer.stop()
        self.ui.startBtn.setEnabled(True) 
        self.clearPlot()
        # TODO: stop the motor

        print("Test stopped")

    def manual_control(self):
        ''' Gets called when the manual control dial is moved by user'''
        val = self.ui.manualDial.value()
        self.ui.currentpositionLabel.setText(str(val) + "%")
        print("manual control dial changed %i" %val)

        # TODO: Use the dial value to control the motor position
    def incrementSpeed(self):
        ''' Gets called when increment button is triggered by user'''
        self.ui.decrementBtn.setEnabled(True)
        self.ui.decrementBtn.setIcon(QtGui.QIcon('Resources/decrementBtn.png'))
        if self.setSpeed >= self.upperSpeedLim:
            self.ui.incrementBtn.setEnabled(False)
            self.ui.incrementBtn.setIcon(QtGui.QIcon('Resources/incrementBtn_disabled.png'))
            print("Hit speed upper limit")
        else:
            self.ui.incrementBtn.setEnabled(True)
            self.ui.incrementBtn.setIcon(QtGui.QIcon('Resources/incrementBtn.png'))
            self.setSpeed += self.speedStepSize
            self.ui.setpullspeedLabel.setText(str(self.setSpeed))
        self.setSpeedLine.setValue(self.setSpeed)
        print("Current set speed %i" %self.setSpeed)

    def decrementSpeed(self):
        self.ui.incrementBtn.setEnabled(True)
        self.ui.incrementBtn.setIcon(QtGui.QIcon('Resources/incrementBtn.png'))
        if self.setSpeed<=self.lowerSpeedLim:
            self.ui.decrementBtn.setEnabled(False)
            self.ui.decrementBtn.setIcon(QtGui.QIcon('Resources/decrementBtn_disabled.png'))
            print("Hit speed lower limit")
        else:
            self.ui.decrementBtn.setEnabled(True)
            self.ui.decrementBtn.setIcon(QtGui.QIcon('Resources/decrementBtn.png'))
            self.setSpeed -= self.speedStepSize
            self.ui.setpullspeedLabel.setText(str(self.setSpeed))
        self.setSpeedLine.setValue(self.setSpeed)
        print("Current set speed %i" %self.setSpeed)

    def logData(self,toolFlag=False):
        ''' Gets called when user check/uncheck the log data group box'''
        # Prompt where to save the file
        if self.ui.dataloggingGroup.isChecked():
            self.ui.dataloggingGroup.setTitle('Data Logging [enabled]')
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
            self.ui.dataloggingGroup.setTitle('Data Logging [disabled]')
            print('Data logging is disabled')

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    # Use win.showFullScreen() to show the application in full screen on start up
    #win.showFullScreen()
    win.show()
    sys.exit(app.exec_())
main()