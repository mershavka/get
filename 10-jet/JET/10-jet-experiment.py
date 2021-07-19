import RPi.GPIO as GPIO
import time
import datetime
import jetFunctions as func
import numpy as np

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
motor = [15, 14, 3, 2]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
directionPin = 27

motorPhases = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

func.initGPIOjet()       

try: 
    data = []
    #DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

    mm = 71

    a = 940 #колво шагов в мм - ввести
    l = 40 #мm, длина стержня - ввести
     # длина стержня в шагах

    duration = 0.5 # время записи данных  фикс 
    x = 100  # кол-во точек
    L = a*30/l # длина 30mm в шагах

    n = int(L/x) # дельта между точками в шагах

    for i in range (x):
        data = func.measure(duration)
        mean = sum(data)/len(data)
        data.append(mean)
        func.stepForward(n)

    #for i in range (x):
        #func.stepBackward(n)
    #time.sleep(2)
    func.stepBackward(540)
    func.stepForward(35)


    np.savetxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/{}mm.txt'.format(mm), data, fmt='%d')

finally:

    func.deinitGPIOjet()