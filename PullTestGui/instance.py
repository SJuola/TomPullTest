#!usr/bin/env/python3
'''
Author: Kiet Tran
Init Date: 12/21/2018
Company: Colder Products Company
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from InitUI import Ui_MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = QMainWindow( )
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.showMaximized()
    sys.exit(app.exec_())

main()
