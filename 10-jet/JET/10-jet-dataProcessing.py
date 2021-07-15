import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
from mpl_toolkits.mplot3d import Axes3D

# Enter constants and names

L = 30 # в мм
low = 0 #давление в паскалях в атм-е
high = 68 #давление в паскалях в потоке


dir = '/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/'
files = os.listdir(dir)

FN_LP = files[0]
FN_HP = files[5]

FN_L01 = files[8]
FN_L11 = files[3]
FN_L21 = files[2]
FN_L31 = files[9]
FN_L41 = files[7]
FN_L51 = files[1]
FN_L61 = files[6]
FN_L71 = files[4]


# Load data from files

LP = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_LP)
HP = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_HP)

L01 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L01)
L11 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L11)
L21 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L21)
L31 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L31)
L41 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L41)
L51 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L51)
L61 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L61)
L71 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/' + FN_L71)

# Calculate mean and k

meanLP = sum(LP)/len(LP)
meanHP = sum(HP)/len(HP)

k = (high - low)/(meanHP - meanLP)

# Smoothing plots

N1 = 20

L01_Smothed = (np.convolve(L01, np.ones((N1,))/N1, mode = 'valid'))
L11_Smothed = (np.convolve(L11, np.ones((N1,))/N1, mode = 'valid')) 
L21_Smothed = (np.convolve(L21, np.ones((N1,))/N1, mode = 'valid'))  
L31_Smothed = (np.convolve(L31, np.ones((N1,))/N1, mode = 'valid'))  
L41_Smothed = (np.convolve(L41, np.ones((N1,))/N1, mode = 'valid'))  
L51_Smothed = (np.convolve(L51, np.ones((N1,))/N1, mode = 'valid'))  
L61_Smothed = (np.convolve(L61, np.ones((N1,))/N1, mode = 'valid'))  
L71_Smothed = (np.convolve(L71, np.ones((N1,))/N1, mode = 'valid'))  

# Centering and creating lengthlines 

num = len(L01)-N1+1 # num of elements in smoothed plots

lengthlineL01 = np.linspace(-L/2, L/2, num) - list(L01_Smothed).index(np.max(L01_Smothed))*(L-4)/(num)+15
lengthlineL11 = np.linspace(-L/2, L/2, num) - list(L11_Smothed).index(np.max(L11_Smothed))*L/(num)+15
lengthlineL21 = np.linspace(-L/2, L/2, num) - list(L21_Smothed).index(np.max(L21_Smothed))*L/(num)+15
lengthlineL31 = np.linspace(-L/2, L/2, num) - list(L31_Smothed).index(np.max(L31_Smothed))*L/(num)+15
lengthlineL41 = np.linspace(-L/2, L/2, num) - list(L41_Smothed).index(np.max(L41_Smothed))*L/(num)+15
lengthlineL51 = np.linspace(-L/2, L/2, num) - list(L51_Smothed).index(np.max(L51_Smothed))*L/(num)+15
lengthlineL61 = np.linspace(-L/2, L/2, num) - list(L61_Smothed).index(np.max(L61_Smothed))*L/(num)+15
lengthlineL71 = np.linspace(-L/2, L/2, num) - list(L71_Smothed).index(np.max(L71_Smothed))*L/(num)+15


# Calculate jet flow

j = [0]*8

for i in range (num):

    j[0] += abs ( (0.00001*L/len(L01))^2*i * ((k*L01[i]-low)*2/1.27)**(1/2) ) # *0.00001 чтобы  было в м
    j[1] += abs ( (0.00001*L/len(L01))^2*i * ((k*L11[i]-low)*2/1.27)**(1/2) )
    j[2] += abs ( (0.00001*L/len(L01))^2*i * ((k*L21[i]-low)*2/1.27)**(1/2) )
    j[3] += abs ( (0.00001*L/len(L01))^2*i * ((k*L31[i]-low)*2/1.27)**(1/2) )
    j[4] += abs ( (0.00001*L/len(L01))^2*i * ((k*L41[i]-low)*2/1.27)**(1/2) )
    j[5] += abs ( (0.00001*L/len(L01))^2*i * ((k*L51[i]-low)*2/1.27)**(1/2) )
    j[6] += abs ( (0.00001*L/len(L01))^2*i * ((k*L61[i]-low)*2/1.27)**(1/2) )
    j[7] += abs ( 0.00001*L/len(L01)*i * ((k*L71[i]-low)*2/1.27)**(1/2) )

j = [i*2*1.27* np.pi for i in j]


# Create 2D plot

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'Центрированный график зависимости P(x)', xlabel = 'x, мм', ylabel = 'Давление P, Па')

ax.plot(lengthlineL01, k*L01_Smothed, label = '1mm')
ax.plot(lengthlineL11, k*L11_Smothed, label = '11mm')
ax.plot(lengthlineL21, k*L21_Smothed, label = '21mm')
ax.plot(lengthlineL31, k*L31_Smothed, label = '31mm')
ax.plot(lengthlineL41, k*L41_Smothed, label = '41mm')
ax.plot(lengthlineL51, k*L51_Smothed, label = '51mm')
ax.plot(lengthlineL61, k*L61_Smothed, label = '61mm')
ax.plot(lengthlineL71, k*L71_Smothed, label = '71mm')
ax.legend()


# Create 3D plot

fig3D = plt.figure()
ax3D = fig3D.add_subplot(111, projection='3d')
ax3D.set(title = 'Распределение скоростей потока в затопленной струе', xlabel = 'x, мм', ylabel = 'Расстояние от сопла l, мм', zlabel = 'Скорость потока V, м/с')

ax3D.plot(lengthlineL01, [1]*(num), ((k*L01_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [11]*(num), ((k*L11_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [21]*(num), ((k*L21_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [31]*(num), ((k*L31_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [41]*(num), ((k*L41_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [51]*(num), ((k*L51_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [61]*(num), ((k*L61_Smothed-low)*2/1.27)**(1/2))
ax3D.plot(lengthlineL01, [71]*(num), ((k*L71_Smothed-low)*2/1.27)**(1/2))


# Create plot of jet flow

figJet = plt.figure()
axJet = figJet.add_subplot(111)
axJet.set(title = 'График зависимости Q(l)', xlabel = 'Расстояние от сопла l, мм', ylabel = 'Расход Q, м.куб./с')
axJet.grid(color = 'gray', linestyle = ':')

axJet.plot(np.linspace(1, 71, 8), j)

plt.show()

fig.savefig('/home/pi/Repositories/10-jet-Plots/all.png')
fig3D.savefig('/home/pi/Repositories/10-jet-Plots/3Dall.png')
figJet.savefig('/home/pi/Repositories/10-jet-Plots/Jet.png')
