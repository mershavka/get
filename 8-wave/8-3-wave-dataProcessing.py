import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
from mpl_toolkits.mplot3d import Axes3D


# Enter variables and directory of files

low = 1 #уровень воды в см
high = 5 #уровень воды в см

dir = '/home/pi/Repositories/get/8-wave/DATA'

FN_data = ''

FN_HL = ''
FN_LL = ''


# Load data from files
data = np.loadtxt(dir + data)

HL = np.loadtxt(dir + FN_HL)
LL = np.loadtxt(dir + FN_LL)


# Calculate mean and k
meanLP = sum(LP)/len(LP)
meanHP = sum(HP)/len(HP)

k = (high - low)/(meanHP - meanLP)


# Smoothing plots
dataSP = []
N1 = 20

for i in range (len(data)):
    dataSP.append(np.convolve(data[i], np.ones((N1,))/N1, mode = 'valid'))


# Centering and creating lengthlines 
lengths = []
num = len(data[0])-N1+1 # num of elements in smoothed plots

for i in range (len(dataSP)):
    lengths.append(np.linspace(-L/2, L/2, num) - list(dataSP[i]).index(np.max(dataSP[i]))*L/(num)+15)

lengths[0] = np.linspace(-L/2, L/2, num) - list(dataSP[0]).index(np.max(dataSP[0]))*(L-4)/(num)+15


# Calculate jet flow
Q = [0]*8

for j in range (len(dataSP)):

    for i in range(len(dataSP[j])):
        Q[j] += abs ( (0.001*L/len(dataSP[j]) * ((0.001*L/len(dataSP[j])*i) * ((k*dataSP[j][i]-low)*2/1.27)**(1/2) )))

Q = [i*1.27*np.pi for i in Q]

for i in range(len(dataSP)):
    print(len(lengths[i]), ' ', len(dataSP[i]))

# Create 2D plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'Центрированный график зависимости P(x)', xlabel = 'x, мм', ylabel = 'Давление P, Па')

for i in range(len(dataSP)):
    print(len(lengths[i]), ' ', len(dataSP[i]))
    ax.plot(lengths[i], k*dataSP[i], label = '{}mm'.format(10*i+1))

ax.legend()


# Create 3D plot
fig3D = plt.figure()
ax3D = fig3D.add_subplot(111, projection='3d')
ax3D.set(title = 'Распределение скоростей потока в затопленной струе', xlabel = 'x, мм', ylabel = 'Расстояние от сопла l, мм', zlabel = 'Скорость потока V, м/с')

for i in range(len(dataSP)):
    ax3D.plot(lengths[i], [10*i+1]*(num), ((k*dataSP[i]-low)*2/1.27)**(1/2))


# Create plot of jet flow
figJet = plt.figure()
axJet = figJet.add_subplot(111)
axJet.set(title = 'График зависимости Q(l)', xlabel = 'Расстояние от сопла l, мм', ylabel = 'Расход Q, кг/с')
axJet.grid(color = 'gray', linestyle = ':')

axJet.plot(np.linspace(1, 71, 8), Q)

plt.show()


#Save plots
fig.savefig('/home/pi/Repositories/10-jet-Plots/all.png')
fig3D.savefig('/home/pi/Repositories/10-jet-Plots/3Dall.png')
figJet.savefig('/home/pi/Repositories/10-jet-Plots/Jet.png')