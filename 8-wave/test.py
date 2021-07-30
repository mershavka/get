import RPi.GPIO as GPIO
import time
import datetime

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

test = 22 



GPIO.setmode(GPIO.BCM)
GPIO.setup(test , GPIO.IN)

while True:

    if GPIO.input(test) == 0:
        print('hello!')
        time.sleep(0.1)
    if GPIO.input(test) == 1: 
        print ('loser!')
        time.sleep(0.1)
    