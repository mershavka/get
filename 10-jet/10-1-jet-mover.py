import RPi.GPIO as GPIO
import time
import jetFunctions as func

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
directionPin = 27
enablePin = 14
stepPin = 2

try:
    steps = 0

    while True:
        n = input('Enter number of steps: ')

        if n == 's':
            print(steps, ' steps')

        elif n == 'z':
            steps = 0
            print(steps, ' steps')

        elif n == 'q':
            print(steps, ' steps')
            break

        else:

            n = int(n)
            if n < 0:
                func.stepBackward(abs(n))

            if n > 0:
                func.stepForward(n)

            steps += n

finally:

    func.deinitGPIOjet()