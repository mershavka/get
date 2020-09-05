import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

top = 18
bottom = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup([top, bottom], GPIO.OUT)

GPIO.output(top, GPIO.HIGH)
GPIO.output(bottom, GPIO.LOW)

def num2dac(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(dac[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

try:
    while True:
      value = int(input('Enter value (-1 to exit) > '))
      
      if value < 0:
          break

      num2dac(value)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')