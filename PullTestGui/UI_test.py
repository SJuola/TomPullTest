# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("/*---New Edit--*/\n"
"QWidget{background: black;}\n"
"QTabBar{ background: #c9cbcd; color: rgb(9,9,9)}\n"
"QPushButton:hover, QPushButton:pressed{background-color: rgba(255,255,255,0.6)}\n"
"QGroupBox{color: white}\n"
"QGroupBox > QLabel{color: white}\n"
"QGroupBox > QLineEdit, QToolButton{background: white}\n"
"QGroupBox:indicator{background: white; color: black; width: 18px; height: 18px}\n"
"QGroupBox  {\n"
"    border: 0.5px solid rgba(255,255,255, 0.3);\n"
"    border-radius: 3px;\n"
"    margin-top: 27px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    background-color: transparent;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px ;\n"
"}\n"
"\n"
"\n"
"/*QMainWindow{background: #e8e8e8}*/\n"
"QPushButton:disabled{ background: #999; color: black}\n"
"QPushButton{ height: 45px; background: #f3f4f5}\n"
"PlotWidget{ color: rgb(35, 85, 244) !important}\n"
"/*QGroupBox{background: #e5e5e5}*/\n"
"\n"
"\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setWhatsThis("")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab1.sizePolicy().hasHeightForWidth())
        self.Tab1.setSizePolicy(sizePolicy)
        self.Tab1.setObjectName("Tab1")
        self._2 = QtWidgets.QGridLayout(self.Tab1)
        self._2.setContentsMargins(11, 11, 11, 11)
        self._2.setSpacing(15)
        self._2.setObjectName("_2")
        self.dataloggingGroup = QtWidgets.QGroupBox(self.Tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataloggingGroup.sizePolicy().hasHeightForWidth())
        self.dataloggingGroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.dataloggingGroup.setFont(font)
        self.dataloggingGroup.setTitle("Data Logging")
        self.dataloggingGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dataloggingGroup.setCheckable(True)
        self.dataloggingGroup.setChecked(False)
        self.dataloggingGroup.setObjectName("dataloggingGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dataloggingGroup)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton = QtWidgets.QToolButton(self.dataloggingGroup)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dataloggingGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.dataloggingGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self._2.addWidget(self.dataloggingGroup, 1, 0, 1, 1)
        self.controlGroup = QtWidgets.QGroupBox(self.Tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlGroup.sizePolicy().hasHeightForWidth())
        self.controlGroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.controlGroup.setFont(font)
        self.controlGroup.setTitle("Control")
        self.controlGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.controlGroup.setObjectName("controlGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controlGroup)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stopBtn = QtWidgets.QPushButton(self.controlGroup)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        self.stopBtn.setFont(font)
        self.stopBtn.setObjectName("stopBtn")
        self.gridLayout_2.addWidget(self.stopBtn, 4, 0, 1, 3)
        self.startBtn = QtWidgets.QPushButton(self.controlGroup)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("background: #006cb1; color: white")
        self.startBtn.setObjectName("startBtn")
        self.gridLayout_2.addWidget(self.startBtn, 3, 0, 1, 3)
        self.setpullspeedLabel = QtWidgets.QLabel(self.controlGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setpullspeedLabel.sizePolicy().hasHeightForWidth())
        self.setpullspeedLabel.setSizePolicy(sizePolicy)
        self.setpullspeedLabel.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(30)
        self.setpullspeedLabel.setFont(font)
        self.setpullspeedLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.setpullspeedLabel.setObjectName("setpullspeedLabel")
        self.gridLayout_2.addWidget(self.setpullspeedLabel, 0, 1, 1, 1)
        self.pullspeedunitLabel = QtWidgets.QLabel(self.controlGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pullspeedunitLabel.sizePolicy().hasHeightForWidth())
        self.pullspeedunitLabel.setSizePolicy(sizePolicy)
        self.pullspeedunitLabel.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(16)
        self.pullspeedunitLabel.setFont(font)
        self.pullspeedunitLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pullspeedunitLabel.setObjectName("pullspeedunitLabel")
        self.gridLayout_2.addWidget(self.pullspeedunitLabel, 1, 1, 1, 1)
        self.incrementBtn = QtWidgets.QPushButton(self.controlGroup)
        self.incrementBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incrementBtn.sizePolicy().hasHeightForWidth())
        self.incrementBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(35)
        self.incrementBtn.setFont(font)
        self.incrementBtn.setStyleSheet("")
        self.incrementBtn.setObjectName("incrementBtn")
        self.gridLayout_2.addWidget(self.incrementBtn, 0, 2, 2, 1)
        self.decrementBtn = QtWidgets.QPushButton(self.controlGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decrementBtn.sizePolicy().hasHeightForWidth())
        self.decrementBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(35)
        self.decrementBtn.setFont(font)
        self.decrementBtn.setObjectName("decrementBtn")
        self.gridLayout_2.addWidget(self.decrementBtn, 0, 0, 2, 1)
        self._2.addWidget(self.controlGroup, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Tab1, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Tab2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.Tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.currentpositionLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentpositionLabel.sizePolicy().hasHeightForWidth())
        self.currentpositionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(16)
        self.currentpositionLabel.setFont(font)
        self.currentpositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentpositionLabel.setObjectName("currentpositionLabel")
        self.gridLayout_4.addWidget(self.currentpositionLabel, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.manualDial = QtWidgets.QDial(self.Tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualDial.sizePolicy().hasHeightForWidth())
        self.manualDial.setSizePolicy(sizePolicy)
        self.manualDial.setProperty("value", 50)
        self.manualDial.setObjectName("manualDial")
        self.verticalLayout_4.addWidget(self.manualDial)
        self.tabWidget.addTab(self.Tab2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.plotarea = PlotWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotarea.sizePolicy().hasHeightForWidth())
        self.plotarea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.plotarea.setFont(font)
        self.plotarea.setObjectName("plotarea")
        self.gridLayout.addWidget(self.plotarea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tom Accelerated Pull Test"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Current logging directory"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.setpullspeedLabel.setText(_translate("MainWindow", "50"))
        self.pullspeedunitLabel.setText(_translate("MainWindow", "in/s"))
        self.incrementBtn.setText(_translate("MainWindow", "+"))
        self.decrementBtn.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Test Mode"))
        self.groupBox.setTitle(_translate("MainWindow", "Current Position "))
        self.currentpositionLabel.setText(_translate("MainWindow", "50%"))
        self.label.setText(_translate("MainWindow", "[relative to rail length]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("MainWindow", "Manual Control"))

from pyqtgraph import PlotWidget
