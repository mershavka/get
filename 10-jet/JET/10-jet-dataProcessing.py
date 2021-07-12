import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import jetFunctions as pp

# Enter constants and names

low = #давление в паскалях в атм
high = #давление в паскалях в потоке

FN_LP = #имя файла с калибловки в атм
FN_HP = #имя файла с калибловки в потоке

FN_L10 = #Имя файла измерения 1я длина
FN_L20 = #Имя файла измерения 2я длина
FN_L30 = #Имя файла измерения 3я длина

# Load data from files

LP = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/' + FN_LP)
HP = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/' + FN_HP)

L10 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/' + FN_HP)
L20 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/' + FN_HP)
L30 = np.loadtxt('/home/pi/Repositories/get/10-jet/DATAjet/' + FN_HP)

# Smoothing plots

# Graph smoothing for puls wave

# Calculate mean and k

meanLP = sum(LP)/len(LP)
meanHP = sum(HP)/len(HP)

k = (high - low)/(meanHP - meanLP
)

# Create timelines

# Calculations of puls

# Create plots