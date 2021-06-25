import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

comp = 4
troyka = 17

levels = 2 ** bits
scale = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, GPIO.HIGH)

def num2dac(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(dac[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)
 
def adc():

    value = 0
    up = True

    for i in range(0, bits):
        delta = 2 ** (bits - 1 - i)
        value = value + delta * (1 if up else -1)

        num2dac(value)
        sleep(0.01)

        dacModeSig = GPIO.input(comp) == 0
        up = False if dacModeSig else True

    return value

try:
    while True:
        measure = adc()
        print('Digital code: {:3d}, Analog value: {:.2f} V'.format(measure, measure * scale))

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
    
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed') 