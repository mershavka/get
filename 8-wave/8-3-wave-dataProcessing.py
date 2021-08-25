import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pathlib
import os

import waveFunctions as func


# Enter variables and directory of files
dir = '/home/pi/Repositories/get/8-wave/DATA/'

levels = np.linspace(20, 100, 5)


# Soft files by last change
files = os.listdir(dir)
files = func.softFiles(files)
print(files)


# Load data from files
    # main data
data = np.loadtxt(dir + files[6]) 
files = files[:5]

    # calibrations data
calibrations = []

for i in range (len(files)):
    calibrations.append(np.loadtxt(dir + files[i]))


# Calculate mean, create list of dots
adc = []

for i in calibrations:
    adc.append( sum(calibrations[i]) / len(calibrations[i]) )


# Polynomial selection
degree = 4
yvals = func.polynom(adc, levels, degree)
dataP = func.polynom(data, levels, degree)


# Create calibration plots
for i in range(len(calibrations)):
    func.calibrationPlots(calibrations[i], levels[i])


# Create polynom plot (calibration)
func.polynomPLot(levels, adc, yvals, degree)


# Create DATA plot
func.wavePlot(dataP)