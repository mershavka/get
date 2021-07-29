import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import waveFunctions as func
from mpl_toolkits.mplot3d import Axes3D


# Enter variables and directory of files

low = 85 #уровень воды для калибровки, мм
high = 160 #уровень воды для калибровки, мм

dir = '/home/pi/Repositories/get/8-wave/DATA/'

FN_data = '28.07.2021-13:31:59.txt'
FN_LL = '28.07.2021-13:18:42.txt'
FN_HL = '28.07.2021-13:08:01.txt'

# Load data from files
data = np.loadtxt(dir + FN_data)
LL = np.loadtxt(dir + FN_LL)
HL = np.loadtxt(dir + FN_HL)

# Calculate mean and k
meanLL = sum(LL)/len(LL)
meanHL = sum(HL)/len(HL)

k = (high - low)/(meanHL - meanLL)
print(k)

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