import RPi.GPIO as GPIO
import time

leds = [24]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(leds, GPIO.OUT)

p = GPIO.PWM(24, 120)

for n in range(10):

    for i in range(100):
        p.start(i)
        time.sleep(0.003)
        p.stop()

    for i in range(100):
        p.start(100 - i)
        time.sleep(0.003)
        p.stop()

GPIO.cleanup()