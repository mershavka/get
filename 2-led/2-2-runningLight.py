import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

count = 24 # кол-во переключений
period = 0.5 # период между зажиганиями

def runningLight(count, period):

    ledNumber = 0

    for i in range(count):

        GPIO.output(leds[ledNumber], 1)
        time.sleep(period)
        GPIO.output(leds[ledNumber], 0)

        if ledNumber <= 6:
            ledNumber = ledNumber+1

        else: 
            ledNumber = ledNumber-7

count = 24 # кол-во переключений
period = 0.1 # период между зажиганиями

# Вызов функции runningLight 
runningLight(count, period)

GPIO.output(leds, 0)
GPIO.cleanup()