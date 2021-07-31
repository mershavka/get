import time
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pathlib
import os

import waveFunctions as func


# Enter variables and directory of files
dir = '/home/pi/Repositories/get/8-wave/DATA/'

levels = np.linspace(20, 100, 5)


#Soft files by last change
files = os.listdir(dir)

for j in range(len(files)):

    for i in range (len(files)-1):

        if os.stat(dir + files[i+1]).st_mtime < os.stat(dir + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a
            
print(files)


# Load data from files
data = np.loadtxt(dir + files[6])

files = files[:5]
calibrations = []

for i in range (len(files)):
    calibrations.append(np.loadtxt(dir + files[i]))


# Calculate mean, create list of dots
adc = []

for i in calibrations:
    adc.append( sum(calibrations[i])/len(calibrations[i]) )


# Polynomial selection
degree = 4
polyK = np.polyfit(adc, levels, degree) #коэф-ы
polynom = np.poly1d(polyK) #уравнение (полином)
print(polynom)

yvals = np.polyval(polynom, adc)

dataP = np.polyval(polynom, data)

# Create calibration plots
for i in range(len(calibrations)):
    func.calibrationPlots(calibrations[i], levels[i])


# Create polynom plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'График зависимости отсчетов АЦП от уровня воды. ', xlabel = 'Уровень воды, мм', ylabel = 'Отсчеты АЦП')
ax.legend()

ax.scatter(levels, adc, label = 'Точки соответствия отсчетов АЦП уровням воды')
ax.plot(yvals, adc, label = 'Подобранный полином {} степени'.format(degree))


# Create DATA plot
DATAfig = plt.figure()
DATAax = DATAfig.add_subplot(111)
DATAax.grid(color = 'gray', linestyle = ':')
DATAax.set(title = 'График зависимости уровня воды от времени. ', xlabel = 'Время, с', ylabel = 'Уровень воды, мм')
DATAax.legend()

DATAax.plot(dataP)

plt.show()

#Save plots
fig.savefig('/home/pi/Repositories/get/8-wave/8-wave-plots/WaveCalibration.png')
DATAfig.savefig('/home/pi/Repositories/get/8-wave/8-wave-plots/FinalWave.png')