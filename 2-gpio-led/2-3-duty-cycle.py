import RPi.GPIO as GPIO
from time import sleep

led = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

period = 0.001
brightness = 0.5
duration = 2

cycles = int(duration / period)
print('Lets blink', cycles, 'times for', duration, 'seconds with', brightness, 'brightness!')

for i in range(cycles):
    GPIO.output(led, GPIO.HIGH)
    sleep(period * brightness)
    GPIO.output(led, GPIO.LOW)
    sleep(period * (1 - brightness))

GPIO.cleanup()
print('GPIO cleanup completed')