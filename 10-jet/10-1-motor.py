import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4

enable = 22
direcion = 23
step = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup([enable, direcion, step], GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def adc():

    timeout = 0.0001
    value = 0
    direction = 1

    for i in range(8):
        delta = 2 ** (8 - i - 1)
        value += delta * direction

        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1

    value += 1 if direction > 0 else 0

    return value

try:
    GPIO.output(enable, 1)
    GPIO.output(direcion, 1)

    for i in range(2000):
        GPIO.output(step, 1)
        GPIO.output(step, 0)
        time.sleep(0.01)

finally:
    GPIO.cleanup()