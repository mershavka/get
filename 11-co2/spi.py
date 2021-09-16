import RPi.GPIO as GPIO

import time

clock  = 18
miso = 23
mosi = 24
cs   = 25

def adcSPI():

    GPIO.output(cs, False)
    data = str()

    for i in range(15):

        GPIO.output(clock, False)

        if GPIO.input(miso):
            data += "1"
        else:
            data += "0"

        GPIO.output(clock, True)

    GPIO.output(cs, True)
    data = data.replace(' ','')[2:14]

    return data