import RPi.GPIO as GPIO
from time import sleep

led = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(led, GPIO.LOW)
    sleep(0.1)

GPIO.cleanup()