#! /usr/bin/python
import curses
import RPi.GPIO as GPIO
from time import sleep


# Configuration
Motor1A = 23
Motor1B = 21
Sensor1 = 25
 
Motor2A = 16
Motor2B = 18
Sensor2 = 20
 
def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Sensor1,GPIO.IN)
 
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Sensor2,GPIO.IN)

def cleanup():
	GPIO.cleanup()
 
def M1forward():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)

def M2forward():
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

def M1backwards():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

def M2backwards():
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
 
def M1stop():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
 
def M2stop():
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)

if __name__ == '__main__':
	setup()

	try:
		while True:
        	time.sleep(10)
	except KeyboardInterrupt:
    	print 'Exiting...'

	cleanup()