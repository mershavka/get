import RPi.GPIO as GPIO
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt

import jetFunctions as func

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
directionPin = 27
enablePin = 14
stepPin = 2

func.initGPIOjet()

try:
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
    data = func.measure(10)
    
    np.savetxt('/home/pi/Repositories/get/10-jet/DATA/calibration_{}.txt'.format(DATE), data, fmt='%d')
    print('Done! Files already saved!')

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