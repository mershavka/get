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

GPIO.output(directionPin, 0)

try:
    i = 0

    while i<=N:

        func.step()
        i +=1
except:
    
    pass

finally:
    func.deinitGPIOjet()