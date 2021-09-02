import RPi.GPIO as GPIO
import time

led = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

for i in range(5):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()