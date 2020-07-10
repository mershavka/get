import RPi.GPIO as GPIO
from time import sleep

cloud = [10, 12, 14, 15, 17, 18, 21, 24, 26]
sun = [13, 16, 19]
fullCloud = cloud + sun

high = GPIO.HIGH
low = GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(fullCloud, GPIO.OUT)
GPIO.output(fullCloud, high)
sleep(0.1)
GPIO.output(fullCloud, low)

value = 0
maxValue = 2 ** len(fullCloud)

print(maxValue)

try:
    while True:
        mask = bin(value)[2:][::-1]
        print('{}: {}'.format(value, mask))

        GPIO.output(fullCloud, low)

        for i in range(0, len(mask)):
            GPIO.output(fullCloud[i], high if mask[i] == '1' else low)

        sleep(0.01)
        value += 1

        if value >= maxValue:
            value = 0

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')

