# import RPi.GPIO as GPIO

import time
import datetime

import numpy as np


# Setting pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
directionPin = 2
enablePin = 3
stepPin = 14

# Functions jet
def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])


def adc():

    timeout = 0.001
    value = 128
    delta = 128

    for i in range(8):
        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1
        num = delta * direction / 2
        value = int(value + num)
        delta = delta / 2

    return value


def initGPIOjet():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(dac, GPIO.OUT)
    GPIO.setup(troykaVoltage, GPIO.OUT)
    GPIO.setup(comparator, GPIO.IN)

    GPIO.setup([directionPin, enablePin, stepPin], GPIO.OUT)


def step():

    GPIO.output(stepPin, 0)
    time.sleep(0.005)
    GPIO.output(stepPin, 1)
    time.sleep(0.005)
    

def stepForward(n):

    GPIO.output(directionPin, 1)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()

    GPIO.output(enablePin, 0)


def stepBackward(n):

    GPIO.output(directionPin, 0)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()

    GPIO.output(enablePin, 0)

    
def measure(duration): 
    
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
    data = []
    value = 0
    
    start = time.time()
    
    while time.time() - start <= duration:
        value = adc()
        data.append(value)
        
    return data


def deinitGPIOjet():
 
    GPIO.output(dac, 0)
    GPIO.output(troykaVoltage, 0)
    GPIO.output([directionPin, enablePin, stepPin], 0)
    
    GPIO.cleanup()