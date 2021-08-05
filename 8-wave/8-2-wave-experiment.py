import RPi.GPIO as GPIO


import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import waveFunctions as func

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17

button = 22

func.initGPIOwave()       

try:
    
    while True:
        if GPIO.input(button) == 0:
            print('не сейчас...')

        if GPIO.input(button) == 1:
            print('ВОТ СЕЙЧАС!!!')
            data = func.measure(20)
            break

    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")        
    np.savetxt('/home/pi/Repositories/get/8-wave/DATA/{}.txt'.format(DATE), data, fmt='%d')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП')
    ax.plot(data, label = 'Количество измерений {}'.format(len(data)))

    ax.legend()

    plt.show()

    fig.savefig('/home/pi/Repositories/8-wave-Plots/wave.png')

finally:

    func.deinitGPIOwave()