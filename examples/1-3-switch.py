import RPi.GPIO as GPIO
import time

led = 14
inputt = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(inputt, GPIO.OUT)

value = GPIO.input(inputt)
state = 0

while True:
    if(value == 0 and GPIO.input(inputt) == 1):
        state = not state 
        GPIO.output(led, state)
        time.sleep(1)

    value = GPIO.input(inputt)