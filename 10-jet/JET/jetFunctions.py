import RPi.GPIO as GPIO
import time
import datetime
import numpy as np

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
motor = [15, 14, 3, 2]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
directionPin = 27

motorPhases = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

def initGPIOjet():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds + dac + motor, GPIO.OUT)
    GPIO.setup(troykaVoltage, GPIO.OUT)
    GPIO.setup(comparator, GPIO.IN)
    GPIO.setup(directionPin, GPIO.OUT)

    GPIO.output(directionPin, 0)
    GPIO.output(troykaVoltage, 1)

initGPIOjet()

def step():
    for i in range (4):
        val = motorPhases[i % len(motorPhases)]
        GPIO.output(motor, val)
        time.sleep(0.001)
    
def stepForward(n):
    GPIO.output(directionPin, 1)
    for i in range(n):
        step()

def stepBackward(n):
    GPIO.output(directionPin, 0)
    for i in range(n):
        step()

def measure(duration): 

    def num2pins(pins, value):
        GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])

    def adc2():

        timeout = 0.001
        value = 128
        delta = 128

        for i in range(8):
            num2pins(dac, value)
            time.sleep(timeout)

            direction = -1 if (GPIO.input(comparator) == 0) else 1
            num = delta * direction / 2
            value = int(value + num)
            delta = delta / 2

        return value
    
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
    data = []
    value = 0
    
    start = time.time()

    GPIO.output(troykaVoltage, duration)
    
    while time.time() - start <= duration:
        value = adc2()
        data.append(value)
        mean = sum(data)/len(data)
        np.savetxt('/home/pi/Repositories/get/10-jet/DATAjet/calibration_{}.txt'.format(DATE), data, fmt='%d')
    return mean

def deinitGPIOjet():
    
    GPIO.output(directionPin, 0)
    GPIO.output(troykaVoltage, 0)
    GPIO.output(leds + dac + motor, 0)

    deinitGPIOjet()
    GPIO.cleanup()
