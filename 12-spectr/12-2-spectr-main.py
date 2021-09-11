import numpy as np
import matplotlib.pyplot as plt
import imageio

import time

import os
from os import read

import spectrFunctions as func

# Enter constants
dir = 'C:/Users/User/Desktop/Repositories/get/12-spectr/DATA/spectr_photos/'
dir1 = 'C:/Users/User/Desktop/Repositories/get/12-spectr/DATA/plots/'

dots = [310, 443, 468, 540] # y1, y2, x1, x2
stripes = [136, 91, 21] # stripe1, stripe2, stripe3 - Oy


# Load data from all files in directory
colors = func.loadData(dir)


# Cut pictures
for i in range (len(colors)):
    colors[i] = func.cutpic(colors[i], dots)


# Polynomial selection
wavelength = func.polynom(stripes, dots, 3)[1]
xScatter = func.polynom(stripes, dots, 3)[0]


# Calculate intensities
intensities = func.intensities(colors, dots)


# Calculate albedos
albedoes = func.albedoes(intensities, 8)

# Create plots
    # polynom plot
func.polynomPlot(xScatter, stripes, 3, dir1)

    # intensisties plot
func.intensitiesPlot(intensities, wavelength, dir1)

    # albedodes plot
func.albedoesPlot(albedoes, wavelength, dir1)
plt.show()