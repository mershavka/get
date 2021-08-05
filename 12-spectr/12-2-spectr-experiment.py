from os import read
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import imageio
from io import BytesIO


# Enter directory of files
dir = '/home/pi/Repositories/get/12-spectr/DATA/FullSpectr'


# Soft files by last change
files = os.listdir(dir)

for j in range(len(files)):
    for i in range (len(files)-1):
        if os.stat(dir + files[i+1]).st_mtime < os.stat(dir + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a  
print(files)


# Load data from files and cut pictures
white = imageio.imread('/home/pi/Repositories/get/12-spectr/DATA/White_StripesSpectr.monochrome')

colors = 0 

for i in range (len(files)):
    colors.append(imageio.imread(dir + files[i]))
    colors[i] = colors[i][290:460, 450:560, :]


# Make monochrome
greypic = []
grey = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114])

for i in colors:   
    greypic.append(grey(colors[i]))


# Colors intensly
intenseAll = []

for i in colors:
    height = colors[i].shape [0]
    width = colors[i].shape [1]
    intense = 0

    for x in range (width):
        for y in range (height):

            if gray[y, x] > 3:
                intense += gray[y, x] 
    intenseAll.append(intense) 


#llll
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


for i in intervals:
    whiteIntense = 0
    colorIntense = 0

    for x in range (width):
        for y in intervals[i]:

            if white[y, x] > 3:
                whiteIntense += white[y, x] 
            if colors[i][y, x] > 3:
                colorIntense += greypic[i][y, x] 

    albedo = colorIntense/whiteIntense
    allAlbedo.append(albedo)
    

