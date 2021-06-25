import RPi.GPIO as GPIO
import time

motor = [15, 14, 3, 2]
leds = [7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)

GPIO.setup(motor + leds, GPIO.OUT)

motorPhases = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

try:
    for i in range (2000):
        val = motorPhases[i % len(motorPhases)]
        GPIO.output(leds, val)
        GPIO.output(motor, val)
        time.sleep(0.01)

finally:
    GPIO.cleanup()