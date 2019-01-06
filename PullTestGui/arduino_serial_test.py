#usr/bin/env python3

import serial 
import time
import sys

class ArduinoSerialCom:
	def __init__(self, portname, baudrate):
		self.ser = serial.Serial(portname, baudrate)
		self.ser.flush()

		#handshake with the Arduino
	def write2Arduino(data):
		self.ser.write(data)
	def readStream():
		data = self.ser.readline()
		print(data)
		return data

def main():
	portname = input("Enter the Arduino port name: ").upper()
	baudrate = int(input("Enter the baudrate: "))
	ard_com = ArduinoSerialCom(portname, baudrate)

	print('Test sending data')


main()
