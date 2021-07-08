import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib

# Enter high and low value of calibration pressure

high = 160
low = 40

SP1 = 120
DP1 = 60
num1 = 8

SP2 = 140
DP2 = 60
num2 = 20

LFN_HC = '08.07.2021-13:26:03_0.009.txt'
LFN_LC = '08.07.2021-13:26:33_0.009.txt'
LFN_MR = '08.07.2021-13:27:51_0.009.txt'
LFN_MF = '08.07.2021-13:29:18_0.009.txt'

# Load data from files

HC = np.loadtxt('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/08.07.2021-13:26:03_0.009.txt')
LC = np.loadtxt('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/08.07.2021-13:26:33_0.009.txt')
MR = np.loadtxt('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/08.07.2021-13:27:51_0.009.txt')
MF = np.loadtxt('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/08.07.2021-13:29:18_0.009.txt')

# Assigning deltas to variables

delta_HC = float(pathlib.Path(LFN_HC).stem[20:])
delta_LC = float(pathlib.Path(LFN_LC).stem[20:])
delta_MR = float(pathlib.Path(LFN_MR).stem[20:])
delta_MF = float(pathlib.Path(LFN_MF).stem[20:])

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

# Calculations of puls

MR_list = list(MR)
MF_list = list(MF)

tSP1 = MR_list.index(SP1)*delta_MR
tDP1 = MR_list.index(DP1)*delta_MR
puls1 = round(60 / (tDP1 - tSP1) * num1)

tSP2 = MF_list.index(SP2)*delta_MF
tDP2 = MF_list.index(DP2)*delta_MF
puls2 = round(60 / (tDP2 - tSP2) * num2)


# Create area for two plots 
# Create fig and ax for all plots

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()
fig5 = plt.figure()
fig6 = plt.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)
ax5 = fig5.add_subplot(111)
ax6 = fig6.add_subplot(111)

# Create grid for plots of pressure

ax1.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax1.grid(which = 'major', color = 'black')           
ax1.grid(which = 'minor', color = 'gray', linestyle = ':')
ax1.set(title = 'График зависимости P(t) при 1-м измерении для калибровки', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

ax2.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax2.grid(which = 'major', color = 'black')           
ax2.grid(which = 'minor', color = 'gray', linestyle = ':')
ax2.set(title = 'График зависимости P(t) при 2-м измерении для калибровки', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

ax3.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax3.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax3.grid(which = 'major', color = 'black')           
ax3.grid(which = 'minor', color = 'gray', linestyle = ':')
ax3.set(title = 'График зависимости P(t), в состоянии покоя.', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

ax4.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax4.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax4.grid(which = 'major', color = 'black')           
ax4.grid(which = 'minor', color = 'gray', linestyle = ':')
ax4.set(title = 'График зависимости P(t), после физической нагрузки.', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

    # Create grid for plots of puls

ax5.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax5.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax5.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax5.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax5.grid(which = 'major', color = 'black')           
ax5.grid(which = 'minor', color = 'gray', linestyle = ':')
ax5.set(title = 'График пульсовой волны в состоянии покоя.', xlabel = 'Время, с')

ax6.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax6.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax6.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax6.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax6.grid(which = 'major', color = 'black')           
ax6.grid(which = 'minor', color = 'gray', linestyle = ':')
ax6.set(title = 'График пульсовой волны после физической нагрузки.', xlabel = 'Время, с')


# Create smoothed plots
 
ax1.plot(timelineHC, k*HC_Smothed, label ='')
ax2.plot(timelineLC, k*LC_Smothed, label ='')
ax3.plot(timelineMR, k*MR_Smothed, label ='')
ax4.plot(timelineMF, k*MF_Smothed, label ='')

# Create points and legends

ax3.scatter(tSP1, SP1, color = 'red', marker='.', label = 'SP - Систолическое давление')
ax3.scatter(tDP1, DP1, color = 'red', marker='.', label = 'DP - Диастолическое давление')
ax3.text(tSP1 + 0.5, SP1, 'SP = {}'.format(SP1))
ax3.text(tDP1 + 0.5, DP1, 'DP = {}'.format(DP1))
ax3.legend()

ax4.scatter(tSP2, SP2, color = 'red', marker='.', label = 'SP - Систолическое давление')
ax4.scatter(tDP2, DP2, color = 'red', marker='.', label = 'DP - Диастолическое давление')
ax4.text(tSP2 + 0.5, SP2, 'SP = {}'.format(SP2))
ax4.text(tDP2 + 0.5, DP2, 'DP = {}'.format(DP2))
ax4.legend()

#Create plots of puls waves

ax5.plot(np.linspace(0, delta_MR*len(pulsWave1), len(pulsWave1)), pulsWave1, label = 'Пульс {}'.format(puls1))
ax5.legend()

ax6.plot(np.linspace(0, delta_MF*len(pulsWave2), len(pulsWave2)), pulsWave2, label = 'Пульс {}'.format(puls2))
ax6.legend()

plt.show()
time.sleep(15)
plt.close()

# Save plot

fig1.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Smoothed_plot_calibration_{}.png'.format(high))
fig2.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Smoothed_plot_calibration_{}.png'.format(low))

fig3.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Smoothed_plot_measure_rest.png')
fig4.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Smoothed_plot_measure_fitnes.png')

fig5.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Puls_wave_rest')
fig6.savefig('/home/pi/Repositories/get/9-blood/FINAL2/DATA2/Puls_wave_fitnes')








