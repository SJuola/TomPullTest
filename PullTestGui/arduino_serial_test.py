#usr/bin/env python3

import serial 
import time
import sys

class ArduinoSerialCom:
	def __init__(self, portname, baudrate):
		self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=0.005)
		self.ser.flushInput()
	def write2Arduino(self,data):
		self.ser.write(data)
	def readStream(self, size=8):
		data = self.ser.read(size)
		return data
	def close(self):
		self.ser.close()
def main():
	portname = input("Enter the Arduino port name: ").upper()
	baudrate = int(input("Enter the baudrate: "))
	ard_com = ArduinoSerialCom(portname, baudrate)

	try:
		while True:
			print("Data received:  " + ard_com.readStream().decode('ascii'))
			cmd = input("Enter a command: ")
			ard_com.write2Arduino(cmd.encode('ascii'))
	except KeyboardInterrupt:
		ard_com.close()
		print('exiting ... ')
main()
