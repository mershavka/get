import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data

data = np.loadtxt('/home/pi/Repositories/get/9-blood/Data/DATA.txt')
timeline = np.loadtxt('/home/pi/Repositories/get/9-blood/Data/TIME.txt')

SP = 131
DP = 64
num = 11

# Calculations of puls

for i in range(len(data)):
    if data[i] == SP:
        tSP = timeline[i]      
    if data[i] == DP:
        tDP = timeline[i]

puls = round(60 / (tDP - tSP) * num)
print(puls)

# Graph smoothing

N1 = 20
new = np.convolve(data, np.ones((N1,))/N1, mode = 'valid')
new1 = new

# Delete timeline elements
timeline1 = timeline
for i in range (N1-1):
    timeline1 = np.delete(timeline1, 0)

# Graph smoothing for puls wave

N2 = 600
line = np.convolve(data, np.ones((N2,))/N2, mode = 'valid')
for i in range (N2-N1):
    new1 = np.delete(new1, 0)
pulsWave = new1 - line

# Delete timeline elements
timeline2 = timeline
for i in range (N2-N1+19):
    timeline2 = np.delete(timeline2, 0)


#Create area for two plots 

fig1 = plt.figure()
fig2 = plt.figure()
ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)

ax1.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))

ax2.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))

ax1.grid(which = 'major', color = 'black')           
ax1.grid(which = 'minor', color = 'gray', linestyle = ':')

ax2.grid(which = 'major', color = 'black')           
ax2.grid(which = 'minor', color = 'gray', linestyle = ':')

ax1.set(title = 'График зависимости P(t)', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')
ax2.set(title = 'График пульсовой волны', xlabel = 'Время, с')

#Create smoothed plot

ax1.plot(timeline1, new, label ='')

ax1.scatter(tSP, SP, color = 'red', marker='.', label = 'SP - Систолическое давление')
ax1.scatter(tDP, DP, color = 'red', marker='.', label = 'DP - Диастолическое давление')

ax1.text(tSP + 0.5, SP, 'SP = {}'.format(SP))
ax1.text(tDP + 0.5, DP, 'DP = {}'.format(DP))
ax1.legend()

#Create plot of puls wave

ax2.plot(timeline2, pulsWave, label = 'Пульс {}'.format(puls))
ax2.legend()

plt.show()

# Save plot

fig1.savefig('/home/pi/Repositories/get/9-blood/Data/Smoothed_plot_{}-{}.png'.format(SP, DP))
fig2.savefig('/home/pi/Repositories/get/9-blood/Data/Puls_wave_{}'.format(puls))