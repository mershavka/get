import RPi.GPIO as GPIO
import time
import datetime
import numpy as np

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
dinPin = 2

def initGPIOco2():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds + dac, GPIO.OUT)
    GPIO.setup(troykaVoltage, GPIO.OUT)
    GPIO.setup(comparator, GPIO.IN)
    GPIO.setup(dinPin, GPIO.OUT)

    GPIO.output(troykaVoltage, 1)


def deinitGPIOco2():
 
    GPIO.output(troykaVoltage, 0)
    
    GPIO.output(leds + dac, 0)
    GPIO.cleanup()
