import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import plotPressure as pp

# Enter high and low value of calibration pressure

high = 160
low = 40

SP1 = 139
tSP1 = 5.1
DP1 = 65
tDP1 = 15.5
num1 = 14

SP2 = 175
tSP2 = 3.4
DP2 = 64
tDP2 = 14.8
num2 = 23

LFN_HC = '08.07.2021-13.26.03_0.009.txt'
LFN_LC = '08.07.2021-13.26.33_0.009.txt'
LFN_MR = '08.07.2021-13.27.51_0.009.txt'
LFN_MF = '08.07.2021-13.29.18_0.009.txt'

# Load data from files

HC = np.loadtxt('/home/pi/Repositories/get/9-blood/DATA/' + LFN_HC)
LC = np.loadtxt('/home/pi/Repositories/get/9-blood/DATA/' + LFN_LC)
MR = np.loadtxt('/home/pi/Repositories/get/9-blood/DATA/' + LFN_MR)
MF = np.loadtxt('/home/pi/Repositories/get/9-blood/DATA/' + LFN_MF)

# Assigning deltas to variac

# Smoothing plots

N1 = 20

HC_Smothed = np.convolve(HC, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления калибровки 1

LC_Smothed = np.convolve(LC, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления калибровки 2

MR_Smothed = np.convolve(MR, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления до физ.нагрузки
MR_Smothed1 = MR_Smothed

MF_Smothed = np.convolve(MF, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления после физ.нагрузки
MF_Smothed1 = MF_Smothed

# Graph smoothing for puls wave

N2 = 600

for i in range (N2-N1):
    MR_Smothed1 = np.delete(MR_Smothed1, 0)
pulsWave1 = MR_Smothed1 - np.convolve(MR, np.ones((N2,))/N2, mode = 'valid') #массив данных для первой пульсовой волны

for i in range (N2-N1):
    MF_Smothed1 = np.delete(MF_Smothed1, 0)
pulsWave2 = MF_Smothed1 - np.convolve(MF, np.ones((N2,))/N2, mode = 'valid') #массив данных для второй пульсовой волны

# Calculate mean and k

meanHC = sum(HC)/len(HC)
meanLC = sum(LC)/len(LC)

k = (high - low)/(meanHC - meanLC)

# Create timelines

timelineHC = np.linspace(0, delta_HC*len(HC_Smothed), len(HC_Smothed))
timelineLC = np.linspace(0, delta_LC*len(LC_Smothed), len(LC_Smothed))
timelineMR = np.linspace(0, delta_MR*len(MR_Smothed), len(MR_Smothed))
timelineMF = np.linspace(0, delta_MF*len(MF_Smothed), len(MF_Smothed))
timelinePuls1 = np.linspace(0, delta_MR*len(pulsWave1), len(pulsWave1))
timelinePuls2 = np.linspace(0, delta_MF*len(pulsWave2), len(pulsWave2))

# Calculations of puls

puls1 = round(60 / (tDP1 - tSP1) * num1)
puls2 = round(60 / (tDP2 - tSP2) * num2)

# Create plots

pp.plotPressure(MR_Smothed, timelineMR, SP1, tSP1, DP1, tDP1, k)
pp.plotPressure(MF_Smothed, timelineMF, SP2, tSP2, DP2, tDP2, k)

pp.plotCalibration(HC_Smothed, timelineHC, high, k)
pp.plotCalibration(LC_Smothed, timelineLC, low, k)

pp.plotPuls(pulsWave1, timelinePuls1, puls1, k)
pp.plotPuls(pulsWave2, timelinePuls2, puls2, k)