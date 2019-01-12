# Author: Kiet Tran
# Init date: 12/21/2018
# Work in progress

from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import sys, time, random
import serial_asyncio
import serial
import numpy        as np
import pyqtgraph    as pg
from   pyqtgraph    import PlotWidget
from   collections  import deque
from   functools    import partial # passing args into slot functions

from UI_test import Ui_MainWindow as uiwindow # Import the Python script exported from Qt Creator .ui file

'''
class SerialCom:
    def __init__(self, port, rate):
        self.reader, self.writer = await serial_asyncio.open_serial_connection(url=port, baudrate=rate)
    async def send(self, msg):
        await self.writer.write(str.encode(msg)) #use encode to convert 
    async def receive(self):
        return await self.reader.readuntil(b'\n') #return the encoder data. Make sure that the Arduino just send the encoder data in this format: value\n
'''
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.refreshRate    = 10 # default sampling interval
        self.setSpeed       = 50 # default pulling speed
        self.upperSpeedLim  = 55 # Upper pulling speed
        self.lowerSpeedLim  = 20 # Lower pulling speed
        self.speedStepSize  = 1  # default increment/decrement step size for increase/decreasing pulling speed
        self.isRunning      = False # True when motor is rotating, else False
        self.logDir         = None
        self.data           = deque() # high performace queue to store velocity data
        
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
        self.ui.toolButton.clicked.connect(partial(     self.logData, True)) # Data logging group
        self.ui.dataloggingGroup.toggled.connect(partial(self.logData, False))
        self.ui.manualDial.valueChanged.connect(        self.manual_control)    # Manual control dial
        
        '''configure velocity plot'''
        self.plotItem = self.ui.plotarea.getPlotItem()
        self.ui.plotarea.setAntialiasing(True)
        #self.plotItem.enableAutoRange(axis="x", enable=True)
        self.plotItem.enableAutoRange(axis="y", enable=True)
        #self.plotItem.setYRange(min=0,max=60,padding=0.1)
        self.plotItem.setXRange(min=0, max=5000, padding=0.1)
        self.plotItem.setLabel('left','Pulling speed [in/s]')
        self.plotItem.setLabel('bottom', 'Time [s]')
        self.plotItem.showAxis('right')
        self.plotItem.showAxis('top')
        self.plotItem.setTitle('<span style="font-family:sans-serif">Pulling Speed over Time</span>')
        self.plotItem.showGrid(x=True, y=True, alpha=0.3)
        print("Plot title and axis labels updated")


        '''Checking the serial port asynchronously
        using asyncio and serial_sync modules
        Check here for tutorials: https://tinkering.xyz/async-serial/
        '''
        '''self.loop = asyncio.get_event_loop()
        #Initialize an instance of the SerialCom class
        self.serial_com = SerialCom(port = '/dev/ttyACM0', rate = 115200)'''

    #Function to send command to Arduino command. Command must follow the serial data format in current.ino
    '''def sendCommand(cmd):
        self.loop.run_until_complete(self.serial_com.send(cmd))
        self.loop.close()
    
    # Function to read the data from the serial port
    def getSerialData():
        # Retrieve data sent from Arduino
        print("Reading serial port asynchronously")
        asyncio.run(getSerialData_async())

    # Implement reading serial data asynchronously
    async def getSerialData_async():
        self.data.append({'x': self.time.elapsed(), 'y': self.serial_com.receive()})'''

    ''' SLOT FUNCTIONS '''
    def updatePlot(self):
        # reading data from serial port asynchronously
        #self.getSerialData()
        self.data.append({'x': self.time.elapsed(), 'y': np.random.uniform(-1, 1)})
        x = [item['x'] for item in self.data]
        y = [item['y'] for item in self.data]
        (self.plotItem.listDataItems())[0].setData(x=x, y=y, pen= pg.mkPen('w', width=1, style=QtCore.Qt.DotLine))

        temp = self.time.elapsed()
        print("Current time: %s" %temp)
        if temp >=5000:
            self.ui.startBtn.setEnabled(True)
            self.timer.stop()
            
            #Write data to file
            if self.logDir==None:
                writePath = '/home/akiet00/Desktop/log_test.csv' # default directory
            else:
                writePath = self.logDir + 'log_test.csv'
            with open(writePath,'w') as file:
                file.writelines('time [miliseconds], velocity [in/s] \n')
                for item in self.data:
                    file.write(str(item['x']) + ',' + str(item['y']) + '\n')
                    if len(self.plotItem.listDataItems())!=0:
                        #self.plotItem.removeItem((self.plotItem.listDataItems())[0]) # Remove the first curve
                        self.ui.plotarea.clear()

    def startTest(self):
        self.time.start()
        self.plotItem.addItem(pg.PlotDataItem())

        self.ui.startBtn.setEnabled(False) # Avoid double clicking issue
        print("Test started")
        # Send commands to motor
        #self.sendCommand('spin:150') #150 is only for testing
        
        # Collect the RPM and plot linear velocity
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(20) #update every 20 miliseconds

    def stopTest(self):
        print("Test stopped")

    def manual_control(self):
        val = self.ui.manualDial.value()
        self.ui.currentpositionLabel.setText(str(val) + "%")
        print("manual control dial changed %i" %val)

    def incrementSpeed(self):
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
            print('Current log dir: %s' %self.logDir)

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
main()