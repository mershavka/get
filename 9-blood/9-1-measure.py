import RPi.GPIO as GPIO
import time
import datetime
import numpy as np
import bloodFunctions as func

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comparator = 4 
troykaVoltage = 17

func.initGPIOblood()

try:
    
    now = datetime.datetime.now()
    DATE = now.strftime("%d.%m.%Y-%H.%M.%S")
  
    t = 20
    measure = []
    value = 0
    
    start = time.time()

    GPIO.output(troykaVoltage, 1)

    while time.time() - start <= t:
        value = func.adc2()
        measure.append(value)

    delta = round(t / int(len(measure)), 3)
    
    np.savetxt('/home/pi/Repositories/get/9-blood/FINAL/DATA/{}_{}.txt'.format(DATE, delta), measure, fmt='%d')
    print('Done! Files already saved!')

finally:
    deinitGPIOblood()
    print('GPIO cleanup completed.')