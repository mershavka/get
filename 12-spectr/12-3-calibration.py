import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read

# Enter directory
dir1 = 'C:/Users/yurko/Desktop/Repositories/get/12-spectr/DATA/Intensity/'
dir2 = 'C:/Users/yurko/Desktop/Repositories/get/12-spectr/DATA/Intensity_plots'

rainbow = ['black', 'red', 'orange', 'yellow', 'green', 'lightgreen', 'blue', 'darkblue', 'crimson', 'grey']

# Soft files by last change
files = os.listdir(dir1)

for j in range(len(files)):
   for i in range (len(files)-1):
        if os.stat(dir1 + files[i+1]).st_mtime < os.stat(dir1 + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a  
print(files)

# Load data from files
intensities = []

for i in range (len(files)):
    intensities.append(np.loadtxt(dir1 + files[i]))


# Calculate Albedo
allColorsAL = []

for i in range (len(intensities)):
    oneColorAL = []

    for y in range (len(intensities[i])): 
       
        albedo = intensities[i][y]/intensities[0][y]
        oneColorAL.append(albedo) 

    allColorsAL.append(oneColorAL)

# Smoothing plots
Salbedo = []
N1 = 10

for i in range (len(allColorsAL)):
    Salbedo.append(np.convolve(allColorsAL[i], np.ones((N1,))/N1, mode = 'valid'))

# Mercury calibration
mercury = [576.96, 546.074, 435.83]
picture = [136, 91, 21]

# Polynomial selection
degree = 3
polyK = np.polyfit(picture, mercury, degree) # коэф-ы полинома
polynom = np.poly1d(polyK) # полином
print(polynom)

yvals = np.polyval(polynom, picture)
mercurySpectr = np.polyval(polynom, np.linspace(0, len(intensities[0]), len(intensities[0]))) 


yvalsAlbedo = []

for i in range(len(Salbedo)):
    yvalsAlbedo[i] = np.polyval(polynom, Salbedo[i])
    
print(len(Salbedo), ' ', len(yvalsAlbedo))

# Create calibration plot
figCalib = plt.figure()
ax = figCalib.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'Зависимость длины волны от номера пикселя (по высоте)', xlabel = 'Номер пикселя', ylabel = 'Длина волны, нм', label = '')

ax.scatter(picture, mercury, label = 'Точки соответствия номеров пикселей длинам волн')
ax.plot(picture, yvals, label = 'Подобранный полином {} степени'.format(degree))
ax.legend(loc=1, bbox_to_anchor=(1, 0.15), prop={'size': 9})

# Create albedo plots
for i in range(len(intensities)):
    Albedofig = plt.figure()
    Albedoax = Albedofig.add_subplot(111)           
    Albedoax.grid(color = 'gray', linestyle = ':')
    Albedoax.set(title = '', xlabel = 'Номер пикселя (нумерация сверху вниз)', ylabel = 'Альбедо')
    
    Albedoax.plot(Salbedo[i], yvalsAlbedo[i], label = rainbow[i], color = rainbow[i])

    Albedofig.savefig(dir2 + '/AlbedoPlot_{}.png'.format(rainbow[i]))

plt.show()




