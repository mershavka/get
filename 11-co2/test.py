import RPi.GPIO as GPIO
import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import spi.py as func

dir = '/home/pi/Repositories/get/10-jet/DATA/spitest.txt'

DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
data = []
value = 0

start = time.time()

while time.time() - start <= duration:
    value = func.adcSPI()
    data.append(value)

np.savetxt(dir, data, fmt='%d')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'График', xlabel = 'Номер измерения', ylabel = 'Отсчеты АЦП', label = 'Количество измеренй = {}'.format(len(data)))

ax.plot(data)

plt.show()

fig.savefig('/home/pi/Repositories/get/10-jet/10-jet-Plots/Ex-plot{}.png'.format(distance))
