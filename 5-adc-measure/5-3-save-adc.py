import RPi.GPIO as GPIO
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt

leds = [21, 20, 16, 12, 7, 8, 25, 23]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

comp = 4

top = 18
bottom = 15

levels = 2 ** bits
scale = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup([top, bottom], GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(top, GPIO.HIGH)
GPIO.output(bottom, GPIO.LOW)

def num2pins(pins, value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(pins[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

def adc():

    value = 0
    up = True

    for i in range(0, bits):
        delta = 2 ** (bits - 1 - i)
        value = value + delta * (1 if up else -1)

        num2pins(dac, value)
        sleep(0.01)

        sampleVoltageIsLessThanDac = GPIO.input(comp) == 0
        up = True if sampleVoltageIsLessThanDac else False

    return value

seconds = float(input('Enter how many seconds to measure > '))
timeout = time.time() + seconds
measure = []

while time.time() < timeout:
    value = adc()
    num2pins(leds, value)
    measure.append(value)

period = seconds / len(measure)

filename = '5-adc-measure/data-period{:.4f}s-scale{:.4f}v.txt'.format(period, scale)
np.savetxt(filename, measure, fmt='%d')

GPIO.cleanup()
print('GPIO cleanup completed')


time = np.asarray(list(range(0, len(measure)))) * period
plt.plot(time, np.asarray(measure) * scale)
plt.show()