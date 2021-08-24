
import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

while True:
    GPIO.output(dac, 0)
    GPIO.output(dac, 1)