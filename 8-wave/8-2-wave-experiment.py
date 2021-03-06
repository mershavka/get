import RPi.GPIO as GPIO

import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import waveFunctions as func

# Setting pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4 
troykaVoltage = 17
button = 22

func.initGPIOwave()       

try:
    
    while True:
        # Button test
        if GPIO.input(button) == 0:
            print('не сейчас...')

        if GPIO.input(button) == 1:
            print('ВОТ СЕЙЧАС!!!')
            data = func.measure(20) # Measure
            break

    # Data storage
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")        
    np.savetxt('/home/pi/Desktop/Repositories/get/8-wave/DATA/{}.txt'.format(DATE), data, fmt='%d')

    # Ceate plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП')
    ax.plot(data, label = 'Количество измерений {}'.format(len(data)))

    ax.legend()

    plt.show()

    # Save plot
    fig.savefig('/home/pi/Desktop/Repositories/get/8-wave/DATA/wave.png')

finally:
    func.deinitGPIOwave()