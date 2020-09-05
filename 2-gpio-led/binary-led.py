import RPi.GPIO as GPIO
from time import sleep

leds = [23, 25, 8, 7, 12, 16, 20, 21]
high = GPIO.HIGH
low = GPIO.LOW

def ledNumber(value):
  mask = bin(value)[2:][::-1]
  
  GPIO.output(leds, low)

  for i in range(0, len(mask)):
    GPIO.output(leds[i], high if mask[i] == '1' else low)

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, high)
sleep(0.1)
GPIO.output(leds, low)

value = 0
maxValue = 2 ** len(leds)

print(maxValue)

try:
    while True:
        ledNumber(value)
        sleep(0.1)
        value += 1

        if value >= maxValue:
            value = 0

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
