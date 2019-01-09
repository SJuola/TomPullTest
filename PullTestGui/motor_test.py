#! usr/bin/env/python3

'''Motor should rotates continuously'''

import piplates.DAQCplate as daq
import time

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
