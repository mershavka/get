import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
from mpl_toolkits.mplot3d import Axes3D


# Enter variables and directory of files
L = 30 # в мм
low = 0 #давление в паскалях в атм-е
high = 51 #давление в паскалях в потоке

dir = 'C:/Users/ksyurko/Desktop/Repositories/get/10-jet/'


# Soft files by last change

files = os.listdir(dir + 'DATA/')

for j in range(len(files)):
    for i in range (len(files)-1):
        if os.stat(dir + 'DATA/'+ files[i+1]).st_mtime < os.stat(dir+ 'DATA/' + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a  
print(files)


# Load data from files
HP = np.loadtxt(dir + 'DATA/' + files[8])
LP = np.loadtxt(dir + 'DATA/' + files[9])

files = files[:8]
data = []

for i in range (len(files)):
    data.append(np.loadtxt(dir + 'DATA/' + files[i]))


# Calculate mean and k
meanLP = sum(LP)/len(LP)
meanHP = sum(HP)/len(HP)

k = (high - low)/(meanHP - meanLP)


# Smoothing plots
dataSP = []
N1 = 20

for i in range (len(data)):
    dataSP.append(abs(np.convolve(data[i], np.ones((N1,))/N1, mode = 'valid') - 55))


# Centering and creating lengthlines 
lengths = []
num = len(data[0])-N1+1 # num of elements in smoothed plots

for i in range (len(dataSP)):
    lengths.append(np.linspace(-L/2, L/2, num) - list(dataSP[i]).index(np.max(dataSP[i]))*L/(num)+15)

lengths[0] = (np.linspace(-L/2, L/2, num) - list(dataSP[0]).index(np.max(dataSP[0]))*L/(num)+14)
lengths[1] = (np.linspace(-L/2, L/2, num) - list(dataSP[1]).index(np.max(dataSP[1]))*L/(num)+14)
lengths[3] = (np.linspace(-L/2, L/2, num) - list(dataSP[3]).index(np.max(dataSP[3]))*L/(num)+14.5)

# Calculate jet flow
Q = [0]*8

for j in range (len(dataSP)):

    for i in range(len(dataSP[j])):
        Q[j] += abs ( (0.001*20/len(dataSP[j]) * ((0.001*20/len(dataSP[j])*i) * ((abs(k*dataSP[j][i]-low)*2/1.27))**(1/2) )))

Q = [i*1.27*np.pi for i in Q]


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
fig.savefig(dir + '10-jet-Plots/all.png')
fig3D.savefig(dir + '10-jet-Plots/3Dall.png')
figJet.savefig(dir + '10-jet-Plots/Jet.png')