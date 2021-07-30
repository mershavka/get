import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import waveFunctions as func
from mpl_toolkits.mplot3d import Axes3D


# Enter variables and directory of files
dir = '/home/pi/Repositories/get/8-wave/DATA/'

#soft files by last change

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
levels = []

for i in range (len(files)):

    levels.append(np.loadtxt(dir + files[i]))

# Calculate mean and k
dots = []

for i in levels:
    dots.append( sum(levels[i])/len(levels[i]) )

np.polyfit(np.linspace(0, 100, 5), dots, 3)

# Smoothing plot
dataS = []
N1 = 100

dataS = np.convolve(data, np.ones((N1,))/N1, mode = 'valid')

# Create 2D plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'График зависимости h(t)', xlabel = 'Время t, с', ylabel = 'Уровень воды, мм')

ax.plot(np.linspace(0, 15, len(dataS)), k*dataS)

plt.show()

#Save plots
fig.savefig('/home/pi/Repositories/8-wave-Plots/finalWave.png')