import serial
import numpy as np
import matplotlib.pyplot as plt
import math
import time


"""
comPort = 8
arduino = None
try:
	arduino = serial.Serial(port="COM8", baudrate=115200, timeout=5)
	time.sleep(0.1)
	print("Found serial")
except:
	print("Could not find serial")
	pass
"""
arduino = None
comPort = 8

def serial_init():
	global arduino
	arduino = serial.Serial(port='COM'+str(comPort), baudrate=115200, timeout=0.5)

def serial_send(s):
	global comPort
	try:
		arduino.write(s.encode('utf-8'))
		arduino.flush()
		#data = arduino.readline().decode().strip()
	except (FileNotFoundError, serial.serialutil.SerialException, NameError) as e:
		print(f"Caught exception: {e}")
		print("Could not find Arduino on COM" + str(comPort))
		comPort = input("Enter new COM port num: COM")
		try:
			arduino = serial.Serial(port='COM'+str(comPort), baudrate=115200, timeout=.1)
			time.sleep(0.1)
			print("Found serial")
		except (FileNotFoundError, serial.serialutil.SerialException):
			pass
		except KeyboardInterrupt:
			return
		
serial_send('f')
"""
time.sleep(0.5)
while arduino is not None:
	try:
		arduino.write('s'.encode('utf-8'))
		arduino.flush()
		#data = arduino.readline().decode().strip()
			
	except (FileNotFoundError, serial.serialutil.SerialException, NameError) as e:
		print(f"Caught exception: {e}")
		print("Could not find Arduino on COM" + str(comPort))
		comPort = input("Enter new COM port num: COM")
		try:
			arduino = serial.Serial(port='COM'+str(comPort), baudrate=115200, timeout=.1)
			time.sleep(0.1)
			print("Found serial")
		except (FileNotFoundError, serial.serialutil.SerialException):
			pass
		except KeyboardInterrupt:
			break
"""