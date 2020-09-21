import RPi.GPIO as GPIO
from time import sleep

leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, GPIO.HIGH)

sleep(1)

GPIO.cleanup()