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
	def readStream(self):
		data = self.ser.readline()
		print(data)
		return data
	def close(self):
		self.ser.close()
def main():
	portname = input("Enter the Arduino port name: ").upper()
	baudrate = int(input("Enter the baudrate: "))
	ard_com = ArduinoSerialCom(portname, baudrate)

	data = 'R'
	print('Test sending data')
	try:
		while True:
			ard_com.readStream()
			time.sleep(2)
			print("Sending data ... %s" %data.encode())
			ard_com.write2Arduino(b'R')
			ard_com.ser.flush()
	except KeyboardInterrupt:
		ard_com.close()
		print('exiting ... ')
main()
