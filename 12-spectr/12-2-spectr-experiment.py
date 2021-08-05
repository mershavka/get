from os import read
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import imageio
from io import BytesIO


# Enter directory of files
dir = '/home/pi/Repositories/get/12-spectr/DATA/newDATAspectr/'


# Soft files by last change
files = os.listdir(dir)

for j in range(len(files)):
    for i in range (len(files)-1):
        if os.stat(dir + files[i+1]).st_mtime < os.stat(dir + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a  
print(files)


# Load data from files, cut and make monochrome pictures
white = imageio.imread(dir + files[1])
grey = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114])  
white = grey(white)

files = files[1:]

colors = []
greypic = []

for i in range (len(files)):
    colors.append(imageio.imread(dir + files[i]))
    colors[i] = colors[i][290:460, 450:560, :]

    grey = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114])  
    greypic.append(grey(colors[i]))

height = greypic[1].shape [0]
width = greypic[1].shape [1]

# intervals
red        = np.arange(800, 630, 1).tolist()
orange     = np.arange(590, 630, 1).tolist() 
yellow     = np.arange(570, 590, 1).tolist() 
lightgreen = np.arange(550, 570, 1).tolist()
green      = np.arange(510, 550, 1).tolist() 
blue       = np.arange(480, 510, 1).tolist() 
darkblue   = np.arange(450, 480, 1).tolist() 
crimson    = np.arange(300, 450, 1).tolist() 

intervals = [red, orange, yellow, lightgreen, green, blue, darkblue, crimson]

allAlbedo = []


for i in range (len(intervals)):
    whiteIntense = 0
    colorIntense = 0

    for x in range (width):
        for y in range (len(intervals[i])):

            if white[y, x] > 0:
                whiteIntense += white[y, x] 
            if greypic[i][y, x] > 0:
                colorIntense += greypic[i][y, x] 
    print (colorIntense, ' ', whiteIntense)
    albedo = colorIntense
    allAlbedo.append(albedo)
print(allAlbedo)

# Save pics
for i in range (len(greypic)):
    imageio.imwrite('/home/pi/Repositories/get/12-spectr/DATA/Color_FullSpectr.monochrome{}.png'.format(i), greypic[i].astype(np.uint8), format='png')