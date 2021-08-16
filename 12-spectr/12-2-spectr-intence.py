import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read

# Enter directory
dir1 = 'C:/Users/yurko/Desktop/Repositories/get/12-spectr/DATA/newDATAspectr/'
dir2 = 'C:/Users/yurko/Desktop/Repositories/get/12-spectr/DATA/Intensity/'
dir3 = 'C:/Users/yurko/Desktop/Repositories/get/12-spectr/DATA/Intensity_plots/'

rainbow = ['black', 'red', 'orange', 'yellow', 'green', 'lightgreen', 'blue', 'darkblue', 'crimson', 'grey']

# Soft files by last change
files = os.listdir(dir1)

# for j in range(len(files)):
#     for i in range (len(files)-1):
#         if os.stat(dir+ 'newDATAspectr/' + files[i+1]).st_mtime < os.stat(dir + 'newDATAspectr/'+ files[i]).st_mtime:
#             a = files[i+1]
#             files[i+1] = files[i]
#             files[i] = a  
# print(files)

files[0] = 'White_FullSpectr.png'
files[1] = 'Red_FullSpectr.png'
files[2] = 'Orange_FullSpectr.png'
files[3] = 'Yellow_FullSpectr.png'
files[4] = 'Lightgreen_FullSpectr.png'
files[5] = 'Green_FullSpectr.png'
files[6] = 'Blue_FullSpectr.png'
files[7] = 'darkBlue_FullSpectr.png'
files[8] = 'Crimson_FullSpectr.png'
files[9] = 'White_StripesSpectr.png'
print (files)

# Load data from files and cut pictures
colors = []

for i in range (len(files)):
    colors.append(imageio.imread(dir1 + files[i]))
    colors[i] = colors[i][310:443, 468:540, :]

height = colors[0].shape [0]
width = colors[0].shape [1]

# Calculate Intensity of colors
allColorsIL = []

for i in range (len(colors)):
    oneColorIL = []
    
    for y in range (height):
        OStrI = 0

        for x in range (width):
                
            if sum(colors[i][y, x, :]) > 0:
                OStrI += sum(colors[i][y, x, :])

        OStrI = int(OStrI/(3*width))  
        oneColorIL.append(OStrI)
    np.savetxt(dir2 + 'intensity_{}'.format(rainbow[i]), oneColorIL, fmt='%d')
    time.sleep(0.05)

    allColorsIL.append(oneColorIL)


# Smoothing plots
Scolors = []
N1 = 10

for i in range (len(allColorsIL)):
    Scolors.append(np.convolve(allColorsIL[i], np.ones((N1,))/N1, mode = 'valid'))


# Create intensity plots   
for i in range (len(allColorsIL)):
    fig = plt.figure()
    ax = fig.add_subplot(111)           
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'Интенсивность цвета', xlabel = 'Номер пикселя (нумерация сверху вниз)', ylabel = 'Интенсивность', label = '{}'.format(rainbow[i]))

    ax.plot(Scolors[i], label = rainbow[i], color = rainbow[i])
    ax.legend()
    

    fig.savefig(dir3 + '/Intensity_plot_{}.png'.format(rainbow[i]))

plt.show() 
