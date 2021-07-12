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

try: 
    data = []
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
    func.initGPIOjet()

    N = 4000 #длина стержня в шагах - ввести
    L = 5 #cm, длина стержня - ввести

    duration = 1 # время записи данных - ввести - скорее всего фикс
    x = 10 # кол-во точек, скорее всего фикс
    l = L/x #cm, на сколько сдвинуть
    n = int(l*N/L) #сдвиг в шагах

    for i in range (x):
        mean = func.measure(duration)
        data.append(mean)
        func.stepForward(n)
        

    for i in range (x):
        mean = func.measure(duration)
        data.append(mean)
        func.stepBackward(n)

    np.savetxt('/home/pi/Repositories/get/10-jet/DATAjet/{}.txt'.format(DATE), data, fmt='%d')

finally:

    func.deinitGPIOjet()