import time
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pathlib
import os


levels = np.linspace(20, 100, 5)
adc = [20, 90, 150, 205, 230]
data = [240, 239, 239, 238, 236, 230, 229, 229, 227, 225,225,220,218,218,219,216,203,202,200,195,190,190,187,186,183,179,176,175,170,163,160,150,139,120,107,100, 85,70,45,20]

polyadc = np.polyfit(adc, levels, 4)
p = np.poly1d(polyadc) #уравнение (полином)

print(p)
print()

yvals = np.polyval(p, adc) #значение
print(yvals)
print()

dataP = []
lol = []

#for i in range (300):
   #lol.append(np.polyval(p, i))

dataP = np.polyval(p, data)
    
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(lol)
# plt.show()

# Create 2D plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'График зависимости отсчетов АЦП от уровня воды. ', xlabel = 'Уровень воды, мм', ylabel = 'Отсчеты АЦП')

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.grid(color = 'gray', linestyle = ':')
ax1.set(title = 'График зависимости уровня воды от времени. ', xlabel = 'Время, с', ylabel = 'Уровень воды, мм')

ax.scatter(levels, adc)
ax.plot(yvals, adc)
ax1.plot(dataP)
plt.show()


    