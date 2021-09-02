import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pathlib
import os

import waveFunctions as func


# Enter variables and directory of files
dir = 'C:/Users/User/Documents/Repositories/get/8-wave/DATA/'


# Soft files by last change
files = os.listdir(dir)
for j in range(len(files)):

    for i in range (len(files)-1):

        if os.stat(dir + files[i+1]).st_mtime < os.stat(dir + files[i]).st_mtime:
            a = files[i+1]
            files[i+1] = files[i]
            files[i] = a
print(files)


# Load data from files
    # main data
data = np.loadtxt(dir + files[5]) 
files = files[:5]

    # calibrations data
calibrations = []

for i in range (len(files)):
    calibrations.append(np.loadtxt(dir + files[i]))


# Calculate mean, create list of dots
adc = []

for i in range (len(calibrations)):
    adc.append( sum(calibrations[i]) / len(calibrations[i]) )


levels = np.linspace(0, len(data), len(data))
levels1 = np.linspace(20, 100, 5)

# Polynomial selection
degree = 4
yvals = func.polynom(adc, levels1, degree)
dataP = func.polynom(data, levels, degree)


# Create calibration plots
for i in range(len(calibrations)):
    func.calibrationPlots(calibrations[i], levels[i])


# Create polynom plot (calibration)
func.polynomPlot(levels, adc, yvals, degree)


# Create DATA plot
func.wavePlot(dataP)