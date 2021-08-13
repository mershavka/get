import RPi.GPIO as GPIO
import time
import jetFunctions as func

directionPin = 2
enablePin = 3
stepPin = 14

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