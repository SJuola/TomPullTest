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
        MainWindow.resize(827, 530)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    background: black;\n"
"    color: white;\n"
"    font: 11pt \"Rockwell\";\n"
"}\n"
"\n"
"graphicsView\n"
"{\n"
"    background: rgb(180,180,180);\n"
"}\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 471, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 91, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 10, 91, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(630, 10, 67, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(630, 60, 67, 41))
        self.label_2.setObjectName("label_2")
        self.dial = QtWidgets.QDial(self.centralWidget)
        self.dial.setGeometry(QtCore.QRect(550, 260, 201, 191))
        self.dial.setAutoFillBackground(False)
        self.dial.setObjectName("dial")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 180, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 220, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))
        self.pushButton_4.setText(_translate("MainWindow", "Log"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


