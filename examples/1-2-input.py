import RPi.GPIO as GPIO
import time

led = 14
inputt = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(inputt, GPIO.OUT)

while True:
    
    GPIO.output(led, GPIO.input(inputt))