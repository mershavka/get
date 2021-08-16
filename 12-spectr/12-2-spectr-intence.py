import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read

# Enter directory
dir1 = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/newDATAspectr/'
dir2 = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/Intensity/'

rainbow = ['black', 'red', 'orange', 'yellow', 'green', 'lightgreen', 'blue', 'darkblue', 'crimson']

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
whiteIL = []

for i in range (len(colors)):
    oneColorIL = []
    
    for y in range (height):
        OStrI = 0

        for x in range (width):
                
            if sum(colors[i][y, x, :]) > 0:
                OStrI += sum(colors[i][y, x, :])

        OStrI = int(OStrI/(3*width))  
        oneColorIL.append(OStrI)

    np.savetxt(dir2 + 'intensity_{}'.format(i), oneColorIL, fmt='%d')

    allColorsIL.append(oneColorIL)

