#! /usr/bin/python
import curses
import RPi.GPIO as GPIO
from time import sleep


# Configuration
Motor1A = 23
Motor1B = 21
Sensor1 = 15
 
Motor2A = 16
Motor2B = 18
Sensor2 = 22
 
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

def forwardUntilObstacle():
    M1forward()
    M2forward()

    obstacle = False
    while not obstacle:
        if not GPIO.input(Sensor1):
            obstacle = True
        if not GPIO.input(Sensor2):
            obstacle = False

    M1stop()
    M2stop()

if __name__ == '__main__':
    setup()

    try:
        while True
            forwardUntilObstacle()
            M1backwards()
            M2backwards()
            sleep(0.2)
            M1forward()
            sleep(0.2)
            M2forward()

    except KeyboardInterrupt:
        print 'Exiting...'

    cleanup()