#! usr/bin/env/python3

'''Motor should rotates continuously'''

import piplates.DAQCplate as daq
import RPi.GPIO as gpio
import time
import datetime

try:
	while True:
		daq.setDOUTbit(0,0) #turn on pin 0
		daq.setDOUTbit(1,0) #turn on pin 1
		time.sleep(0.2)
		daq.clrDOUTbit(0,0) #turn off pin 0
		daq.clrDOUTbit(1,0) #turn off pin 1
		time.sleep(0.2)
except KeyboardInterrupt:
	print("Exitting ...")

class RPMMeasurement:
	'''@param: daq is an instance of the piPlate daqplate'''
	def __init__(self, daq):
		self.daq = daq
		self.daq.intEnable(0) #enable interrupt from the DAQCplate
		self.chanAPin = 0
		self.chanBPin = 1

		'''Enable interrupt on channel A and channel B'''
		self.daq.enableDINint(self.chanAPin, 0, 'b')
		self.dag.enableDINint(self.chanBPin, 0, 'b')

		#Setup interrupt on RPi pin 22
		gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
		gpio.add_event_detect(22, GPIO.FALLING, callback= self.count)
		self.counter = 0
		self.timer_start = datetime.datetime.now()
	def count(self): #Callback function to be call when an interrupt happens
		sefl.counter += 1
		if self.counter = 0:
			self.timer_start = datetime.datetime.now()
		if self.counter >=200:
			self.calcRPM( datetime.datetime.now()-self.timer_start)
			self.counter = 0 # start counting again
	def calcRPM(self, delTime):
		RPM = self.counter/delTime
		print("RPM: %i" %RPM)
		return RPM

