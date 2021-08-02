import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
from mpl_toolkits.mplot3d import Axes3D

ex = 2
data = np.loadtxt('/home/pi/Repositories/get/10-jet/DATA/experiment{}.txt'.format(ex))
print(data)

# Smoothing plots
dataS = []
N1 = 20
dataS = np.convolve(data, np.ones((N1,))/N1, mode = 'valid')
print(dataS)


# Create 2D plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'Сглаженый график эксперимента {}'.format(ex), xlabel = 'x, мм', ylabel = 'Отсчеты АЦП')
ax.plot(dataS)

plt.show()

fig.savefig('/home/pi/Repositories/get/10-jet/10-jet-Plots/testingEx-S-plot{}.png'.format(ex))
