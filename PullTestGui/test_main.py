#!usr/bin/env/python3

# Author: Kiet Tran
# Init date: 12/21/2018
# Work in progress

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import sys, serial, time, signal
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from functools import partial

# Import the Python script exported from Qt Creator .ui file
from UI_test import Ui_MainWindow as uiwindow

# Slot function to handle signal when "+" button is pressed
@pyqtSlot(name="increment_speed")
def incrementSpeed():
    global setSpeed, ui
    upperLim = 55
    ui.decrementBtn.setEnabled(True)
    if setSpeed>=upperLim:
        ui.incrementBtn.setEnabled(False)
        print("Hit speed upper limit")
    else:
        ui.incrementBtn.setEnabled(True)
        setSpeed += speedStepSize
        ui.setpullspeedLabel.setText(str(setSpeed))
    print("Current set speed %i" %setSpeed)

# Slot function to handle signal when "-" button is pressed
@pyqtSlot(name="decrement_speed")
def decrementSpeed():
    global setSpeed, ui
    lowerLim = 20
    ui.incrementBtn.setEnabled(True)
    if setSpeed<=lowerLim:
        ui.decrementBtn.setEnabled(False)
        print("Hit speed lower limit")
    else:
        ui.decrementBtn.setEnabled(True)
        setSpeed -= speedStepSize
        ui.setpullspeedLabel.setText(str(setSpeed))
    print("Current set speed %i" %setSpeed)

# Slot function to handle signal when "Log Data" button is pressed
# @param: toolFlag indicates whether the signal comes from clicking
# on the tool button instead of checking the data logging group checkbox
@pyqtSlot(bool, name="log_data")
def logData(toolFlag=False):
    global dirname, window, ui

    # Prompt where to save the file
    if ui.dataloggingGroup.isChecked():
        if (ui.lineEdit.text() and toolFlag) or not ui.lineEdit.text():
            """ 
            Prompt user to select a directory EITHER when there's already an existing log directory 
            path but user clicks on the directory tool button OR when the current directory path is
            actually empty
            """
            dirname = str(QFileDialog.getExistingDirectory(parent=window, caption="Select a folder to save log file"))
            ui.lineEdit.setText(dirname)
            print("Logging data to ... %s" %dirname)
    else:
        print('Current log dir: %s' %dirname)

# Slot function to handle signal when the "manualDial" dial
# is released after it has been moved
@pyqtSlot(name="manual_control_dial")
def manual_control():
    global ui
    val = ui.manualDial.value()
    ui.currentpositionLabel.setText(str(val) + "%")
    print("manual control dial changed %i" %val)

# Slot function to update the plot, the update
# rate is set by the global refreshRate
@pyqtSlot(name="update_plot")
def updatePlot():
    print('data')

# Slot function to handle signal when "Start" button is pressed
@pyqtSlot(name="start_test")
def startTest():
    #ui.startBtn.setEnabled(False) # Avoid double clicking issue
    print("Test started")
    # Send commands to motor

    # Collect the RPM
    global refreshRate
    timer = QTimer()
    timer.timeout.connect(updatePlot)
    timer.start(refreshRate)
    print("i'm here")
    
    # Convert from RPM to linear speed

    # Plot data

    # Log data

    #curTime = time.time()
    """if (time.time()-curTime)>=5000.0:
        timer.stop()    #relase resource
        ui.startBtn.setEnabled(True)"""

# Wire up the pressed/slider change events of each UI
# component with the appropriate callback functions
def signal_and_slots_setup(ui):
    ui.incrementBtn.clicked.connect(incrementSpeed)
    ui.decrementBtn.clicked.connect(decrementSpeed)
    ui.startBtn.clicked.connect(startTest)
    #ui.logdataBtn.clicked.connect(logData)
    ui.toolButton.clicked.connect(partial(logData, True))
    ui.dataloggingGroup.toggled.connect(partial(logData, False))
    ui.manualDial.valueChanged.connect(manual_control)

def setupPlotArea():
    global ui
    #ui.plotarea.setContentsMargins(-5.0, -5.0, -5.0, -5.0)
    plotItem = ui.plotarea.getPlotItem()
    plotItem.enableAutoRange(axis="x", enable=True)
    plotItem.enableAutoRange(axis="y", enable=True)
    #plotItem.setYRange(min=0,max=60,padding=0.1)
    plotItem.setLabel('left','Pulling speed [in/s]')
    plotItem.setLabel('bottom', 'Time [s]')
    plotItem.showAxis('right')
    plotItem.showAxis('top')
    plotItem.setTitle('<span style="font-family:sans-serif">Pulling Speed over Time</span>')
    plotItem.showGrid(x=True, y=True, alpha=0.3)
    print("Plot title and axis labels updated")

def main():
    global window, ui, setSpeed, speedStepSize, dirname, refreshRate #dirname is the direcotory to save log data
    
    # setup global varibles
    refreshRate     = 10    #update plot every 10 miliseconds
    setSpeed        = 50    # default pulling speed, unit in/s
    speedStepSize   = 1     # default increment/decrement step size for increasing/decreasing pulling speed 
    dirname = "/"           # default directory to store log file

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = uiwindow()
    ui.setupUi(window)
    setupPlotArea()

    # Test plotting
    x = np.random.normal(size=10000)
    y = np.sin(x)
    ui.plotarea.plot(x,y, pen=None, symbol='+')

    signal_and_slots_setup(ui)

    window.showFullScreen()
    sys.exit(app.exec_())

    signal.signal(signal.SIGINT, signal.SIG_DFL)
main()
