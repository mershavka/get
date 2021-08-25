import RPi.GPIO as GPIO

import time
import datetime

import numpy as np

import waveFunctions as func

# Setting pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]

comparator = 4 
troykaVoltage = 17
button = 22

func.initGPIOwave()

try:

    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")

    data = func.measure(10) # measure
    
    # Data storage
    np.savetxt('/home/pi/Repositories/get/8-wave/DATA/{}.txt'.format(DATE), data, fmt='%d')
    print('Done! Files already saved!')

finally:
    func.deinitGPIOwave()