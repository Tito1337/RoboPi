#! /usr/bin/python
import curses
import RPi.GPIO as GPIO
from time import sleep


# Configuration
Motor1A = 23
Motor1B = 21
 
Motor2A = 16
Motor2B = 18
 
def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
 
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)

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

def getKey():
	screen = curses.initscr()
	try:
	    curses.noecho()
	    curses.curs_set(0)
	    screen.keypad(1)
	    event = screen.getch()
	finally:
	    curses.endwin()
    return event

if __name__ == '__main__':
	setup()

	while True:
	if event == curses.KEY_LEFT:
    	print("Left Arrow Key pressed")
	elif event == curses.KEY_RIGHT:
    	print("Right Arrow Key pressed")
	else:
    	print(event)

	cleanup()