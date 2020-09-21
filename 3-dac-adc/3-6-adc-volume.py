import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

comp = 4
troyka = 17

top = 18
bottom = 15

levels = 2 ** bits
scale = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
# GPIO.setup([top, bottom], GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, GPIO.HIGH)

# GPIO.output(top, GPIO.HIGH)
# GPIO.output(bottom, GPIO.LOW)

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

        sampleVoltageIsLessThanDac = GPIO.input(comp) == 1
        up = True if sampleVoltageIsLessThanDac else False

    return value

try:
    while True:
        value = adc()

        shift = (8 - int((value + 5) / 32))
        volume = 255 >> shift

        num2pins(leds, volume)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')