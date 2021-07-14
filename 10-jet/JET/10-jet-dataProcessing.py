import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
from mpl_toolkits.mplot3d import Axes3D

# Enter constants and names

L = 0.03
low = 0 #давление в паскалях в атм
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

L01_Smothed = (np.convolve(L01, np.ones((N1,))/N1, mode = 'valid'))/10 
L11_Smothed = (np.convolve(L11, np.ones((N1,))/N1, mode = 'valid'))/10 
L21_Smothed = (np.convolve(L21, np.ones((N1,))/N1, mode = 'valid'))/10  
L31_Smothed = (np.convolve(L31, np.ones((N1,))/N1, mode = 'valid'))/10  
L41_Smothed = (np.convolve(L41, np.ones((N1,))/N1, mode = 'valid'))/10  
L51_Smothed = (np.convolve(L51, np.ones((N1,))/N1, mode = 'valid'))/10  
L61_Smothed = (np.convolve(L61, np.ones((N1,))/N1, mode = 'valid'))/10  
L71_Smothed = (np.convolve(L71, np.ones((N1,))/N1, mode = 'valid'))/10  

# Centering and creating lengthlines 

lengthlineL01 = np.linspace(-15, 15, len(L01)-19) - list(L01_Smothed).index(np.max(L01_Smothed))*26/(len(L01)-19)+15
lengthlineL11 = np.linspace(-15, 15, len(L11)-19) - list(L11_Smothed).index(np.max(L11_Smothed))*30/(len(L11)-19)+15
lengthlineL21 = np.linspace(-15, 15, len(L21)-19) - list(L21_Smothed).index(np.max(L21_Smothed))*30/(len(L21)-19)+15
lengthlineL31 = np.linspace(-15, 15, len(L31)-19) - list(L31_Smothed).index(np.max(L31_Smothed))*30/(len(L31)-19)+15
lengthlineL41 = np.linspace(-15, 15, len(L41)-19) - list(L41_Smothed).index(np.max(L41_Smothed))*30/(len(L41)-19)+15
lengthlineL51 = np.linspace(-15, 15, len(L51)-19) - list(L51_Smothed).index(np.max(L51_Smothed))*30/(len(L51)-19)+15
lengthlineL61 = np.linspace(-15, 15, len(L61)-19) - list(L61_Smothed).index(np.max(L61_Smothed))*30/(len(L61)-19)+15
lengthlineL71 = np.linspace(-15, 15, len(L71)-19) - list(L71_Smothed).index(np.max(L71_Smothed))*30/(len(L71)-19)+15

# Calculate jet flow

j = [0]*8

for k in range (len(L01)-19):
    j[0] += abs(L/len(L01)*((L01[k]-low)*2/1.27)**(1/2))
    j[1] += abs(L/len(L01)*((L11[k]-low)*2/1.27)**(1/2))
    j[2] += abs(L/len(L01)*((L21[k]-low)*2/1.27)**(1/2))
    j[3] += abs(L/len(L01)*((L31[k]-low)*2/1.27)**(1/2))
    j[4] += abs(L/len(L01)*((L41[k]-low)*2/1.27)**(1/2))
    j[5] += abs(L/len(L01)*((L51[k]-low)*2/1.27)**(1/2))
    j[6] += abs(L/len(L01)*((L61[k]-low)*2/1.27)**(1/2))
    j[7] += abs(L/len(L01)*((L71[k]-low)*2/1.27)**(1/2))

j = [i*np.pi for i in j]

# Create 2D plot

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(lengthlineL01, L01_Smothed, label = '1mm')
ax.plot(lengthlineL11, L11_Smothed, label = '11mm')
ax.plot(lengthlineL21, L21_Smothed, label = '21mm')
ax.plot(lengthlineL31, L31_Smothed, label = '31mm')
ax.plot(lengthlineL41, L41_Smothed, label = '41mm')
ax.plot(lengthlineL51, L51_Smothed, label = '51mm')
ax.plot(lengthlineL61, L61_Smothed, label = '61mm')
ax.plot(lengthlineL71, L71_Smothed, label = '71mm')
ax.legend()

# Create 3D plot

fig3D = plt.figure()
ax3D = fig3D.add_subplot(111, projection='3d')

ax3D.plot(lengthlineL01, [10]*(len(L01)-19), L01_Smothed)
ax3D.plot(lengthlineL01, [20]*(len(L11)-19), L11_Smothed)
ax3D.plot(lengthlineL01, [30]*(len(L21)-19), L21_Smothed)
ax3D.plot(lengthlineL01, [40]*(len(L31)-19), L31_Smothed)
ax3D.plot(lengthlineL01, [50]*(len(L41)-19), L41_Smothed)
ax3D.plot(lengthlineL01, [60]*(len(L51)-19), L51_Smothed)
ax3D.plot(lengthlineL01, [70]*(len(L61)-19), L61_Smothed)
ax3D.plot(lengthlineL01, [80]*(len(L71)-19), L71_Smothed)

# Create plot of jet flow

figJet = plt.figure()
axJet = figJet.add_subplot(111)
axJet.plot(np.linspace(1, 71, 8), j)

plt.show()

fig.savefig('/home/pi/Repositories/10-jet-Plots/all.png')
fig3D.savefig('/home/pi/Repositories/10-jet-Plots/3Dall.png')