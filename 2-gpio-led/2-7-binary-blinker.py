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
    value = 0

    while True:
      value = value + 1
      value = value % 256
      mask = num2led(value)
      print(mask)
      sleep(0.1)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')