import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troykaVoltage = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(8)])

def adc():

    timeout = 0.5
    value = 0
    direction = 1

    for i in range(7):
        delta = 2 ** (8 - i - 1)
        value += delta * direction

        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1

        print(value, delta, direction)

    num2pins(dac, value + 1)
    time.sleep(timeout)

    if (GPIO.input(comparator) == 1):
        value += 1

    return value

try:
    GPIO.output(troykaVoltage, 1)

    while True:
        value = adc()
        num2pins(leds, value)
        print(value)

finally:
    GPIO.cleanup()