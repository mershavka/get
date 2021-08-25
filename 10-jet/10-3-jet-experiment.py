import RPi.GPIO as GPIO

import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import jetFunctions as func

# Setting pins
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
    data = []
    distance = 71

    l = 40 #длина калибровки, мм
    a = 695 #колво шагов в длине калибровки (40 мм)

    duration = 1 # время записи данных 
    b = 30 # длина дистанции
    x = 100  # кол-во точек
    L = a*b/l # длина дистанции в шагах

    d = int(L/x) # дельта между точками в шагах

    dataFin = []
    
    # Experiment
    for i in range (x):
        data = func.measure(duration)
        mean = sum(data)/len(data)
        dataFin.append(mean)
        time.sleep(0.01)

        print(i)

        func.stepForward(d)
    
    # Data storage
    np.savetxt('/home/pi/Repositories/get/10-jet/DATA/{}mm.txt'.format(distance), dataFin, fmt='%d')

    # Return to starting position
    for i in range (x):
        func.stepBackward(d)
    func.stepBackward(15)

    # Create experiment plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График', xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП', label = 'Количество измеренй = {}'.format(len(data)))

    ax.plot(dataFin)

    plt.show()

    # Save plot
    fig.savefig('/home/pi/Repositories/get/10-jet/10-jet-Plots/Ex-plot{}.png'.format(distance))

finally:
    func.deinitGPIOjet()