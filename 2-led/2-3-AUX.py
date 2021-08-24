import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
aux = [22, 23, 27, 18, 15, 14, 3, 2]


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    
    for i in range(8):

        if GPIO.input(aux[i]) == 0:
            GPIO.output(leds[i], 1)
            
        else:
            GPIO.output(leds[i], 0)