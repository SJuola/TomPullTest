#!usr/bin/env/python3

# Author: Kiet Tran
# Init date: 12/21/2018
# Work in progress

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import sys
import time
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget, GraphicsView
from functools import partial

# Import the Python script exported from Qt Creator .ui file
from UI import Ui_MainWindow as uiwindow

# Slot function to handle signal when "+" button is pressed
# @param: speedLabel is the Qt Label that shows the current set pulling speed
@pyqtSlot(name="increment_speed")
def incrementSpeed(speedLabel):
    global setSpeed, ui
    upperLim = 55
    ui.decrementBtn.setEnabled(True)
    if setSpeed>=upperLim:
        ui.incrementBtn.setEnabled(False)
        print("Hit speed upper limit")
    else:
        ui.incrementBtn.setEnabled(True)
        setSpeed += speedStepSize
        speedLabel.setText(str(setSpeed))
    print("Current set speed %i" %setSpeed)

# Slot function to handle signal when "-" button is pressed
# @param: speedLabel is the QtLabel that shows the current set pulling speed
@pyqtSlot(name="decrement_speed")
def decrementSpeed(speedLabel):
    global setSpeed, ui
    lowerLim = 20
    ui.incrementBtn.setEnabled(True)
    if setSpeed<=lowerLim:
        ui.decrementBtn.setEnabled(False)
        print("Hit speed lower limit")
    else:
        ui.decrementBtn.setEnabled(True)
        setSpeed -= speedStepSize
        speedLabel.setText(str(setSpeed))
    print("Current set speed %i" %setSpeed)

# Slot function to handle signal when "Start" button is pressed
@pyqtSlot(name="start_test")
def startTest():
    print("Test started")
    # Send commands to motor

    # Collect the RPM

    # Convert from RPM to linear speed

    # Plot data

    # Log data

# Slot function to handle signal when "Log Data" button is pressed
@pyqtSlot(name="log_data")
def logData():
    global dirname, window
    # Prompt where to save the file
    dirname = str(QFileDialog.getExistingDirectory(parent=window, caption="Select a folder to save log file"))
    print("Logging data to ... %s" %dirname) 

# Slot function to handle signal when the "manualDial" dial
# is released after it has been moved
# @param: dial is a QtDial
# @param: currentPositionLabel is the QtLabel that shows the current
# manual position. Expressed in percentage
@pyqtSlot(name="manual_control_dial")
def manual_control(dial, currentPositionLabel):
    val = dial.value()
    currentPositionLabel.setText(str(val))
    print("manual control dial changed %i" %val)

# Wire up the pressed/slider change events of each UI
# component with the appropriate callback functions
def signal_and_slots_setup(ui):
    ui.incrementBtn.clicked.connect(partial(incrementSpeed, ui.setpullspeedLabel))
    ui.decrementBtn.clicked.connect(partial(decrementSpeed, ui.setpullspeedLabel))
    ui.startBtn.clicked.connect(startTest)
    ui.logdataBtn.clicked.connect(logData)
    ui.manualDial.valueChanged.connect(partial(manual_control, ui.manualDial, ui.currentPositionLabel))

def setupPlotArea():
    global ui
    ui.plotarea.setContentsMargins(0.0, 0.0, 0.0, 0.0)
    plotItem = ui.plotarea.getPlotItem()
    plotItem.enableAutoRange(axis="x", enable=True)
    plotItem.setLabel('left','Pulling speed [in/s]')
    plotItem.setLabel('bottom', 'Time [s]')
    plotItem.setTitle('<h3 style="font-family: Monospace">Pulling Speed over Time</h3>')
    #plotItem.autoRange(padding="5px")
    #plotItem.showGrid(x=False, y=True, alpha=0.6)
    print("Plot title and axis labels updated")

def main():
    global window, ui, setSpeed, speedStepSize, dirname #dirname is the direcotory to save log data

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = uiwindow()
    ui.setupUi(window)
    setupPlotArea()

    # Test plotting
    x = np.random.normal(size=10000)
    y = np.sin(x)
    ui.plotarea.plot(x,y)

    setSpeed = 50
    speedStepSize = 1

    signal_and_slots_setup(ui)

    window.show()
    sys.exit(app.exec_())

main()