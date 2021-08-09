from os import read
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import imageio
from io import BytesIO


# Enter directory of files
dir = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/'


# Soft files by colors
files = os.listdir(dir + 'newDATAspectr/')

files[0] = 'White_FullSpectr.png'
files[1] = 'Red_FullSpectr.png'
files[2] = 'Orange_FullSpectr.png'
files[3] = 'Yellow_FullSpectr.png'
files[4] = 'Lightgreen_FullSpectr.png'
files[5] = 'Green_FullSpectr.png'
files[6] = 'Blue_FullSpectr.png'
files[7] = 'darkBlue_FullSpectr.png'
files[8] = 'Crimson_FullSpectr.png'
print (files)

# Load data from files, cut and make monochrome pictures
colors = []

for i in range (len(files)):
    colors.append(imageio.imread(dir + 'newDATAspectr/' + files[i]))
    colors[i] = colors[i][310:443, 468:540, :]

height = colors[1].shape [0]
width = colors[1].shape [1]

# Load intervals (in pixels)
intervals = []

for i in range (8): 
    interval = np.loadtxt(dir + 'interval_{}'.format(i))
    intervals.append(interval)

allColorsIL = []
whiteIL = []
allColorsAL = []

# Calculate Intensity and albedo of colors
for i in range (len(colors)):
    oneColorIL = []
    oneColorAL = []
    
    for y in range (height):
        OSI = 0
        WI = 0

        for x in range (width):
                
            if sum(colors[i][y, x, :]) > 0:
                OSI += sum(colors[i][y, x, :])
                WI += sum(colors[0][y, x, :])

        WI = int(WI/(3*width))
        OSI = int(OSI/(3*width))  
        albedo = OSI/WI

        oneColorAL.append(albedo) 

        whiteIL.append(WI)
        oneColorIL.append(OSI)

    allColorsAL.append(oneColorAL)
    allColorsIL.append(oneColorIL)
    

# Create intensity plot   
rainbow = ['black', 'red', 'orange', 'yellow', 'green', 'lightgreen', 'blue', 'darkblue', 'crimson']

fig = plt.figure()
ax = fig.add_subplot(111)           
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = '', xlabel = 'Номер пикселя (нумерация сверху вниз)', ylabel = 'Интенсивность')


for i in range(len(colors)):

    Albedofig = plt.figure()
    Albedoax = Albedofig.add_subplot(111)           
    Albedoax.grid(color = 'gray', linestyle = ':')
    Albedoax.set(title = '', xlabel = 'Номер пикселя (нумерация сверху вниз)', ylabel = 'Альбедо')
    Albedoax.plot(allColorsAL[i], label = rainbow[i], color = rainbow[i])
    ax.legend()

    Albedofig.savefig(dir + '/AlbedoPlot_{}.png'.format(rainbow[i]))

    ax.plot(allColorsIL[i], label = rainbow[i], color = rainbow[i])

ax.legend()

plt.show()

fig.savefig(dir + '/IntensityPlot.png')

# Calculate albedo

for i in range (len(colors)):
    oneColorIL = []
    
    for y in range (height):
        OSI = 0
        for x in range (width):
                
            if sum(colors[i][y, x, :]) > 0:
                OSI += sum(colors[i][y, x, :])
                
        oneColorIL.append(int(OSI/(3*width)))

    allColorsIL.append(oneColorIL)