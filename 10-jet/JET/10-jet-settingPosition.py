import RPi.GPIO as GPIO
import time
import jetFunctions as func

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
motor = [15, 14, 3, 2]

comparator = 4 
troykaVoltage = 17
directionPin = 27

motorPhases = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

N = 6000

func.initGPIOjet()

try:
    steps = 0

    while True:
        n = input('Enter number of steps: ')
        s = str(n)

        if s == 's':
            print(steps, ' steps in one mm')
            break

        n = int(n)
        if n < 0:
            func.stepBackward(abs(n))

        if n > 0:
            func.stepForward(n)

        if n == 0:
            steps = 0

        steps += n

finally:

    func.deinitGPIOjet()