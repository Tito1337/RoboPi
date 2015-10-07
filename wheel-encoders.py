#! /usr/bin/python
import curses
import RPi.GPIO as GPIO
from time import sleep


# Configuration
Motor1A = 23
Motor1B = 21
ProximitySensor1 = 15
RotarySensor1 = 24
 
Motor2A = 16
Motor2B = 18
ProximitySensor2 = 22
RotarySensor2 = 26

# Globals
RotaryCount1 = 0
RotaryCount2 = 0
RotaryLastState1 = False
RotaryLastState2 = False
 
def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(ProximitySensor1,GPIO.IN)
    GPIO.setup(RotarySensor1,GPIO.IN)
 
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(ProximitySensor2,GPIO.IN)
    GPIO.setup(RotarySensor2,GPIO.IN)

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
        if not GPIO.input(ProximitySensor1):
            obstacle = True
        if not GPIO.input(ProximitySensor2):
            obstacle = True

    M1stop()
    M2stop()

def updateEncoders():
    RotaryNewState1 = GPIO.input(RotarySensor1)
    RotaryNewState2 = GPIO.input(RotarySensor2)
    if(RotaryNewState1 != RotaryLastState1):
        RotaryCount1 = RotaryCount1+1
        RotaryLastState1 = RotaryNewState1
    if(RotaryNewState2 != RotaryLastState2):
        RotaryCount2 = RotaryCount2+1
        RotaryLastState2 = RotaryNewState2


if __name__ == '__main__':
    setup()

    try:
        while True:
            M1forward()
            M2forward()
            updateEncoders()
            print("Encoder 1 : " + RotaryCount1)
            print("Encoder 2 : " + RotaryCount2)

    except KeyboardInterrupt:
        print 'Exiting...'

    cleanup()
