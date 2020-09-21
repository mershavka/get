import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 23]
bits = len(leds)

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

number = 128
print(number)

mask = bin(number)
print(mask)

mask = mask[2:]
print(mask)

mask = mask.zfill(bits)
print(mask)


for i in range(0, len(mask)):
    GPIO.output(leds[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)


sleep(1)
GPIO.cleanup()