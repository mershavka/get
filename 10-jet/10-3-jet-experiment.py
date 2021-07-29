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
    data = []
    #DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

    distance = 71

    a = 530 #колво шагов в длине калибровки (30mm)
    l = 30 #калибровка длина

    duration = 1 # время записи данных  фикс 
    x = 100  # кол-во точек фикс
    L = a*30/l # длина 30мм в шагах

    d = int(L/x) # дельта между точками в шагах

    for i in range (x):
        data = func.measure(duration)
        mean = sum(data)/len(data)
        data.append(mean)
        func.stepForward(d)
        
    np.savetxt('/home/pi/Repositories/get/10-jet/DATA/{}mm.txt'.format(distance), data, fmt='%d')

    time.sleep(5)

    for i in range (x):
        func.stepBackward(d)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График', xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП', label = 'Количество измеренй = {}'.format(len(data)))

    ax.plot(data)

    plt.show()
    time.sleep(5)
    plt.close()

finally:

    func.deinitGPIOjet()