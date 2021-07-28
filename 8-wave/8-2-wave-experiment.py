import RPi.GPIO as GPIO
import time
import datetime
import waveFunctions as func
import numpy as np

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
botton = 22

func.initGPIOwave()       

try: 

    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

    data = []
    distance = 71

    np.savetxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/{}.txt'.format(distance), data, fmt='%d')

finally:

    func.deinitGPIOwave()