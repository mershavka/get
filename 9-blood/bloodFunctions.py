import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pathlib

dir = 'C:/Users/ksyurko/Desktop/Repositories/get/9-blood/DATA/'

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4 
troykaVoltage = 17

def initGPIOblood():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)
    GPIO.setup(troykaVoltage, GPIO.OUT)
    GPIO.setup(comparator, GPIO.IN)


def deinitGPIOblood():
    GPIO.output(dac, 0)
    GPIO.output(troykaVoltage, 0)
    GPIO.cleanup()


def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(len(dac))])


def adc():

    timeout = 0.001
    value = 128
    delta = 128

    for i in range(8):
        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1
        num = delta * direction / 2
        value = int(value + num)
        delta = delta / 2

    return value


def plotPressure(measure, timeline, pSP, tSP, pDP, tDP, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости P(t)', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

    ax.plot(timeline, k*measure, label ='')

    ax.scatter(tSP, pSP, color = 'red', marker='.', label = 'SP - Систолическое давление')
    ax.scatter(tDP, pDP, color = 'red', marker='.', label = 'DP - Диастолическое давление')
    ax.text(tSP + 0.5, pSP, 'SP = {}'.format(pSP))
    ax.text(tDP + 0.5, pDP, 'DP = {}'.format(pDP))
    ax.legend()
    
    fig.savefig(dir + 'Smoothed_plot_measure_{}.png'.format(pSP))


def plotCalibration(measure, timeline, level, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости P(t) при калибровке', xlabel = 'Время, с', ylabel = 'Отсчеты АЦП')

    ax.plot(timeline, k*measure, label ='')
    
    fig.savefig(dir + 'Smoothed_plot_calibration_{}.png'.format(level))


def plotPuls(measure, timeline, puls, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График пульсовой волны', xlabel = 'Время, с')
    
    ax.plot(timeline, measure, label = 'Пульс {}'.format(puls))
    ax.legend()

    fig.savefig(dir + 'Puls_wave_{}'.format(puls))