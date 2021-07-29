import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

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

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(8)])

def adc():

    timeout = 0.0011
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

def oneStep():

    stepSize = 10

    for i in range(stepSize):
        GPIO.output(step, 1)
        GPIO.output(step, 0)
        time.sleep(0.05)

def measure():

    count = 20
    sum = 0

    for i in range(count):
        sum += adc()

    return sum / count

try:
    GPIO.output(enable, 1)
    GPIO.output(direcion, 1)

    pressure = []

    for i in range(20):
        pressure.append(measure())
        oneStep()

    plt.plot(pressure)
    plt.show()

    np.savetxt('10-jet/data.txt', pressure, fmt='%03.2f')

finally:
    GPIO.cleanup()