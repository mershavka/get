import RPi.GPIO as GPIO
import time

leds = [23, 25, 8, 7, 12, 16, 20, 21]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(leds, GPIO.OUT)

def lightUp(ledNumber = 0, period = 10):
    for i in 1, 0:
        GPIO.output(leds[ledNumber], i)
        time.sleep(period)

def blink(ledNumber = 0, blinkCount = 10, blinkPeriod = 0.1):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)

def runningLight(count = 1, period = 0.1):
    for n in range(count):
        for i in range(len(leds)):
            GPIO.output(leds[i], GPIO.HIGH)
            time.sleep(period)
            GPIO.output(leds[i], GPIO.LOW)

def runningOne(count = 1, period = 0.1, initialLevel = 0):
    l1 = initialLevel
    l2 = (initialLevel + 1) % 2
    GPIO.output(leds, l1)
    for n in range(count):
        for i in range(len(leds)):
            GPIO.output(leds[i], l2)
            time.sleep(period)
            GPIO.output(leds[i], l1)
    GPIO.output(leds, l2)

def decToBinList(decNumber):
    return [int(i) for i in bin(decNumber)[2:].zfill(8)]

def lightNumber(number):
    binList = decToBinList(number)
    for i in range(len(leds)):
        GPIO.output(leds[i], GPIO.HIGH if binList[i] == 1 else GPIO.LOW)
    print(binList)
        

def runningPatternRight(pattern, repeatNumber = 8):
    for i in range(repeatNumber):
        lightNumber(pattern)
        pattern = (((pattern) % 2) << 7) + (pattern >> 1)
        time.sleep(0.1)

def runningPatternLeft(pattern, repeatNumber = 8):
    for i in range(repeatNumber):
        lightNumber(pattern)
        pattern = (pattern >> 7) + (pattern << 1) % 256
        time.sleep(0.1)

def lightPWM(channel = 0, dutyCycle = 50):
    p = GPIO.PWM(leds[0], 100)
    p.start(dutyCycle)
    time.sleep(1)
    p.stop()


#lightUp(1,1)

#blink(0,5)

#runningOne(10,0.07,0)

runningPatternLeft(0b10000111, 20)

#lightNumber(3)

#print(decToBinList(7))

#lightPWM(1,30)

GPIO.cleanup()


