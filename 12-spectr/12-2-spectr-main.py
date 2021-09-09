import numpy as np
import matplotlib.pyplot as plt
import imageio

import time

import os
from os import read

import spectrFunctions as func

# Enter constants
dir = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/'

dots = [310, 443, 468, 540] # y1, y2, x1, x2
stripes = [136, 91, 21] # stripe1, stripe2, stripe3 - Oy

# Load data from all files in directory
colors = func.loadData(dir)

# Cut pictures
for i in range (len(colors)):
    colors[i] = func.cutpic(colors[i], dots[0], dots[1], dots[2], dots[3])

# Polynomial selection
wavelength = func.polynom(stripes, dots, 3)

# Calculate intensities
intensities = []

for i in range (len(colors)):
    intensities.append(func.intensity())

# Calculate albedos
intensities = []

for i in range (len(colors)):
    intensities.append(func.albedo())


