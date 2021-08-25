import RPi.GPIO as GPIO

import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import jetFunctions as func

# Setting pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]

comparator = 4 
troykaVoltage = 17
directionPin = 2
enablePin = 3
stepPin = 14

func.initGPIOjet()

try:
    # File name
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")

    # Receving data
    data = func.measure(10)
    
    # Data storage
    np.savetxt('/home/pi/Repositories/get/10-jet/DATA/calibration_{}.txt'.format(DATE), data, fmt='%d')
    print('Done! Files already saved!')

    # Creating calibration plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП', label = 'Количество измеренй = {}'.format(len(data)))
    ax.legend()
    
    ax.plot(data)

    plt.show()
    fig.savefig('/home/pi/Repositories/get/10-jet/10-jet-Plots/Calibration-plot{}.png'.format(data[1]))

finally:
    func.deinitGPIOjet()