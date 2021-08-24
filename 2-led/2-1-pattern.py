import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

led = 25

pattern = [1, 0, 0, 0, 0, 1, 1, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(leds + dac, GPIO.OUT)

GPIO.output(leds, pattern)
sleep(1)
GPIO.output(leds, pattern)

GPIO.cleanup()