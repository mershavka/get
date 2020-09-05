import RPi.GPIO as GPIO
from time import sleep
import time
import numpy as np

dac = [10, 9, 11, 5, 6, 13, 19, 26]
top = 18
bottom = 15
comp = 4
high = GPIO.HIGH
low = GPIO.LOW

def dacNumber(value):
  mask = bin(value)[2:][::-1]
  
  GPIO.output(dac, low)

  for i in range(0, len(mask)):
    GPIO.output(dac[i], high if mask[i] == '1' else low)

def adcEasy():
  value = 0

  for i in range(0, 255):
    dacNumber(value)
    sleep(0.001)
    if GPIO.input(comp) > 0:
      return i

    value = i

  return value

def adc():
  value = 127
  for i in range(0, 6):
    dacNumber(value)
    sleep(0.000001)

    delta = 2 ** (6 - i)
    if GPIO.input(comp) > 0:
      value -= delta
    else:
      value += delta
 
  return value

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(top, GPIO.OUT)
GPIO.setup(bottom, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(dac, high)
sleep(0.1)
GPIO.output(dac, low)

GPIO.output(top, high)
GPIO.output(bottom, low)

try:
  count = 1000
  start = time.time()
  results = []

  for i in range(0, count):
      results.append(adc())

  finish = time.time()
  spent = finish - start

  print('{} measures per {} milliseconds. Mean = {}'.format(count, finish - start, np.mean(results)))
  print('Sampling frequency: {0:.2f} Hz'.format(count / spent))

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
