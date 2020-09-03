import RPi.GPIO as GPIO
from time import sleep

leds = [23, 25, 8, 7, 12, 16, 20, 21]
dac = [10, 9, 11, 5, 6, 13, 19, 26]

all = leds + dac

high = GPIO.HIGH
low = GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(all, GPIO.OUT)
GPIO.output(dac, high)
sleep(1)
GPIO.output(dac, low)

value = 0
maxValue = 2 ** len(leds)

print(maxValue)

try:
    while True:
        mask = bin(value)[2:][::-1]
        print('{}: {}'.format(value, mask))

        GPIO.output(leds, low)

        for i in range(0, len(mask)):
            GPIO.output(leds[i], high if mask[i] == '1' else low)

        sleep(0.1)
        value += 1

        if value >= maxValue:
            value = 0

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
