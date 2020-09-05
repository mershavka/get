import RPi.GPIO as GPIO
from time import sleep

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
    sleep(0.3)
    delta = 2 ** (6 - i)
    print(GPIO.input(comp))
    if GPIO.input(comp) < 0:
      value += delta
    else:
      value -= delta
 
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
    while True:
        print(adcEasy())

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
