from os import read
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import imageio
from io import BytesIO


# Enter directory of files
dir = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/'


# Soft files by last change
files = os.listdir(dir + 'newDATAspectr/')

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

# Load data from files, cut and make monochrome pictures
    # White
white = imageio.imread(dir + 'newDATAspectr/' + files[0])
white = white[290:460, 450:560, :]

grey = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114])  
white = grey(white)

files = files[1:]
print(files)

    # Colors
colors = []
greypic = []

for i in range (len(files)):
    colors.append(imageio.imread(dir + 'newDATAspectr/' + files[i]))
    colors[i] = colors[i][290:460, 450:560, :]

    grey = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114])  
    greypic.append(grey(colors[i]))

height = greypic[1].shape [0]
width = greypic[1].shape [1]

# Load intervals (in pixels)
intervals = []

for i in range (8): 
    interval = np.loadtxt(dir + 'interval_{}'.format(i))
    intervals.append(interval)

allAlbedo = []


# Calculate intense and albedo of colors
for i in range (len(intervals)):
    whiteIntense = 0
    colorIntense = 0

    for x in range (width):
        for y in range (len(intervals[i])):

            if white[y, x] > 0:
                whiteIntense += white[y, x] 
                
            if greypic[i][y, x] > 0:
                colorIntense += greypic[i][y, x]

    albedo = colorIntense/whiteIntense
    allAlbedo.append(albedo)


# Create albedo plot
fig = plt.figure()
ax = fig.add_subplot(111)           
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'График зависимости альбедо от длины волны', xlabel = 'Длина волны, нм', ylabel = 'Истиное альбедо')

ax.plot(allAlbedo, label ='')
ax.legend()

plt.show()

fig.savefig(dir + '/albedoPlot.png')


# Save pics
for i in range (len(greypic)):
    imageio.imwrite(dir + 'Color_FullSpectr.monochrome{}.png'.format(i), greypic[i].astype(np.uint8), format='png')
imageio.imwrite(dir + 'White_FullSpectr.monochrome.png'.format(i), white.astype(np.uint8), format='png')
