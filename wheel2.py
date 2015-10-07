#! /usr/bin/python
import curses
import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

# Configuration
Motor1A = 23
Motor1B = 21
ProximitySensor1 = 15
RotarySensor1 = 24
 
Motor2A = 16
Motor2B = 18
ProximitySensor2 = 22
RotarySensor2 = 26

class EncodersThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            updateEncoders()
 
def setup():
    global RotaryLastState1, RotaryLastState2, RotaryCount1, RotaryCount2
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(ProximitySensor1,GPIO.IN)
    GPIO.setup(RotarySensor1,GPIO.IN)
 
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(ProximitySensor2,GPIO.IN)
    GPIO.setup(RotarySensor2,GPIO.IN)
    
    RotaryCount1 = 0
    RotaryCount2 = 0
    RotaryLastState1 = False
    RotaryLastState2 = False

    
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

def moveUntilCount(dir,count1, count2):
    global RotaryCount1, RotaryCount2
    BeforeCount1 = RotaryCount1
    BeforeCount2 = RotaryCount2
    if(dir=='forward'):
        M1forward()
        M2forward()
    elif(dir=='backward'):
        M1backwards()
        M2backwards()
    elif(dir=='right'):
            M1forward()
            M2backwaotrds()
    elif(dir=='left'):
            M1backwards()
            M2forward()
    done1 = False
    done2 = False
    while not (done1 and done2):
      if(RotaryCount1 > BeforeCount1+count1):
        M1stop()
        done1 = True
      if(RotaryCount2 > BeforeCount2+count2):
        M2stop()
        done2 = True


def updateEncoders():
    global RotaryLastState1, RotaryLastState2, RotaryCount1, RotaryCount2
    RotaryNewState1 = GPIO.input(RotarySensor1)
    RotaryNewState2 = GPIO.input(RotarySensor2)
    if(RotaryNewState1 != RotaryLastState1):
        RotaryCount1 = RotaryCount1+1
        RotaryLastState1 = RotaryNewState1
    if(RotaryNewState2 != RotaryLastState2):
        RotaryCount2 = RotaryCount2+1
        RotaryLastState2 = RotaryNewState2


if __name__ == '__main__':
    global RotaryLastState1, RotaryLastState2, RotaryCount1, RotaryCount2
    setup()

    try:
        myThread = EncodersThread()
        myThread.start()
        
        #Avance 1m
        for x in range(1, 18):
           moveUntilCount('forward', 10, 10)

        #Contourne par la gauche
        sleep(1)
        moveUntilCount('left', 14, 15)
        sleep(1)
        for x in range(1, 10):
           moveUntilCount('forward', 10, 10)
        sleep(1)
        moveUntilCount('right',15,14)
        sleep(1)

        #Avance jusqu'à obstacle
        forwardUntilObstacle()

        #Contourne par la droite
        sleep(1)
        moveUntilCount('right',15,14)
        sleep(1)
        for x in range(1, 10):
           moveUntilCount('forward', 10, 10)
        sleep(1)
        moveUntilCount('left', 14, 15)
        sleep(1)

        #Avance 1m
        for x in range(1, 18):
           moveUntilCount('forward', 10, 10)


    except KeyboardInterrupt:
        print 'Exiting...'

    cleanup()
