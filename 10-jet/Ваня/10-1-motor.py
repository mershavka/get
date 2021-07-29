import RPi.GPIO as GPIO
import time

enable = 22
direcion = 23
step = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup([enable, direcion, step], GPIO.OUT)

try:
    GPIO.output(enable, 1)
    GPIO.output(direcion, 1)

    for i in range(2000):
        GPIO.output(step, 1)
        GPIO.output(step, 0)
        time.sleep(0.01)

finally:
    GPIO.cleanup()