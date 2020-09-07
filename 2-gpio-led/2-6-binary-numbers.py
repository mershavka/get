import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 23]
bits = len(leds)

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

def num2led(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(leds[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

    return mask

try:
    while True:
      value = input('Enter value (-1 to exit) > ')
      value = int(value)      
      
      if value < 0:
          break

      mask = num2led(value)
      print('Bit mask for', value, 'is:', mask)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')