#!usr/bin/env/python3
from PyQt5.QtCore import QObject, pyqtSignal
import sys
import serial
import pyqtgraph
import threading

class SerialMonitor(QObject):
    bufferUpdated = pyqtSignal(int)
    def __init__(self, port, rate):
        super(SerialMonitor, self).__init__()
        self.running = False
        self.thread = threading.Thread(target=self.serial_monitor_thread)
        self.port = port
        self.rate = rate

    def start(self):
        try:
            self.ser = serial.Serial(self.port, self.rate)
            self.running = True
            self.thread.start()
            return True
        except Exception as er:
            print('Error open serial port: ', str(er))
            return False
    def stop(self):
        self.running = False
        self.ser.close()

    def serial_monitor_thread(self):
        while self.running is True:
            msg = self.ser.readline()
            if msg:
                try:
                    self.bufferUpdated.emit(int(msg))
                    print("Message received: ", msg)
                except ValueError:
                    print('Wrong data')
            else:
                pass
class SerialSender(QObject):
    sendingData = pyqtSignal(str)
    def __init__(self, port, rate):
        super(SerialSender, self).__init__()
        self.port = port
        self.rate = rate
def main():
    ser = SerialMonitor(port='/dev/ttyACM0', rate=115200)
    if ser.start():
        print("Successfully reading serial port")
