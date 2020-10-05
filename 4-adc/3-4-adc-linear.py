import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

comp = 4
troyka = 17

top = 18
bottom = 15

levels = 2 ** bits
scale = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
# GPIO.setup([top, bottom], GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, GPIO.HIGH)

# GPIO.output(top, GPIO.HIGH)
# GPIO.output(bottom, GPIO.LOW)

def num2dac(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(dac[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

def adc():
    for i in range(0, levels):
        num2dac(i)
        sleep(0.001)
        compValue = GPIO.input(comp) # IS i > SIG
        if compValue == 0:
            return i
    num2dac(0)
    return levels

try:
    while True:
        measure = adc()
        print('Digital value: {:3d}, Analog value: {:.2f}V'.format(measure, measure * scale))

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')