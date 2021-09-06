import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read

def loadData(dir):
    files = os.listdir(dir)
    colors = []

    for i in range (len(files)):
        colors.append(imageio.imread(dir + files[i]))

    return colors

def cutpic(picture, y1, y2, x1, x2):
    picture = picture[y1:y2, x1:x2, :]

    return picture

def polynom(stripes, y1, y2, degree):
    mercury = [576.96, 546.074, 435.83]

    polyK = np.polyfit(stripes, mercury, degree) # коэф-ы полинома
    polynom = np.poly1d(polyK) # полином
    print(polynom)

    yvals = np.polyval(polynom, stripes)
    mercurySpectr = np.polyval(polynom, np.linspace(1, y1-y2, y1-y2)) # Ox for all plots in wavelengths

    return yvals, mercurySpectr


def intensity(color, num):
    whiteIL = []
    allColorsAL = []

    for i in range (len(colors)):
        oneColorIL = []

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

        allColorsIL.append(oneColorIL)

def albedo(colors[i]), num):

    allColorsIL = []
    whiteIL = []
    allColorsAL = []

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

def polynomPlot():

def intensitiesPlot():

def albedosPlot():