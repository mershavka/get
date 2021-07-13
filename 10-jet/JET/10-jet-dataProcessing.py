import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import os
import jetFunctions as pp
import matplotlib.mlab as mlab

# Enter constants and names

L = 10
low = 0 #давление в паскалях в атм
high = 68 #давление в паскалях в потоке


dir = '/home/pi/Repositories/get/10-jet/DATAjet/jet/DATA/'
files = os.listdir(dir)
print(files)

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

L01_Smothed = np.convolve(L01, np.ones((N1,))/N1, mode = 'valid') 
L11_Smothed = np.convolve(L11, np.ones((N1,))/N1, mode = 'valid') 
L21_Smothed = np.convolve(L21, np.ones((N1,))/N1, mode = 'valid') 
L31_Smothed = np.convolve(L31, np.ones((N1,))/N1, mode = 'valid') 
L41_Smothed = np.convolve(L41, np.ones((N1,))/N1, mode = 'valid') 
L51_Smothed = np.convolve(L51, np.ones((N1,))/N1, mode = 'valid') 
L61_Smothed = np.convolve(L61, np.ones((N1,))/N1, mode = 'valid') 
L71_Smothed = np.convolve(L71, np.ones((N1,))/N1, mode = 'valid') 

# Find max

maxL01 = np.max(L01_Smothed) 
maxL11 = np.max(L11_Smothed) 
maxL21 = np.max(L21_Smothed) 
maxL31 = np.max(L31_Smothed) 
maxL41 = np.max(L41_Smothed) 
maxL51 = np.max(L51_Smothed) 
maxL61 = np.max(L61_Smothed) 
maxL71 = np.max(L71_Smothed) 

# Centering
center_index = 0



# Create timelines

timeline = np.linspace(-15, 15, len(L01)-19)

# Create plots

fig = plt.figure()
ax = fig.add_subplot(111)

#ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(5.0))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(1.0))

ax.plot(timeline, L01_Smothed, label = '1mm')
ax.plot(timeline, L11_Smothed, label = '11mm')
ax.plot(timeline, L21_Smothed, label = '21mm')
ax.plot(timeline, L31_Smothed, label = '31mm')
ax.plot(timeline, L41_Smothed, label = '41mm')
ax.plot(timeline, L51_Smothed, label = '51mm')
ax.plot(timeline, L61_Smothed, label = '61mm')
ax.plot(timeline, L71_Smothed, label = '71mm')

ax.legend()
plt.show()

fig.savefig('/home/pi/Repositories/10-jet-Plots/all.png')