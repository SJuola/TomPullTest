#!usr/bin/env/python3
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import sys
import serial
import pyqtgraph
from threading import Thread
import os

class SerialMonitor(QObject):
    bufferUpdated = pyqtSignal(int)
    def __init__(self, port, rate):
        super(SerialMonitor, self).__init__()
        self.running = False
        self.port = port
        self.rate = rate
        self.thread = QThread.create(Function target=self.serial_monitor_thread)
        self.ser = None
    def startThread(self):
        try:
            self.running = True
            self.thread.start()
            return True
        except Exception as er:
            self.running = False
            print('Error starting thread: ', str(er))
            return False
    def stop(self):
        print("closing serial port")
        self.running = False
        self.ser.close()
        #self.thread.join()

    def serial_monitor_thread(self):
        while self.running is True:
            if self.ser == None:
                try:
                    self.ser = serial.Serial(self.port, self.rate)
                except Exception as e:
                    if isinstance(e, serial.serialutil.SerialException):
                        os.system("sudo chmod a+rw " + self.port)
                        self.ser = serial.Serial(self.port, self.rate)
                    else:
                        print("An unknown error occured while opening serial port")
            elif not self.ser.isOpen():
                self.ser.open()
            msg = self.ser.readline()
            print("Message received: ", msg)
            if msg:
                try:
                    self.bufferUpdated.emit(int(msg))
                except ValueError:
                    print('Wrong data')
            else:
                pass
            #self.ser.close()
            #self.stop()
class SerialSender(QObject):
    #sendingData = pyqtSignal(str)
    def __init__(self, port, rate):
        super(SerialSender, self).__init__()
        self.port = port
        self.rate = rate
def main():
    ser = SerialMonitor(port='/dev/ttyACM0', rate=115200)
    try:
        if ser.startThread():
            print("Successfully starting a new thread")
    except KeyboardInterrupt:
        ser.stop()
        print("Ending ...")
if __name__=="__main__":
    main()