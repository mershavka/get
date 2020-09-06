import numpy as np
import matplotlib.pyplot as plt

measure = np.random.randint(255, size = 1000)
period = 0.001
scale = 0.013

filename = '4-adc-measure/data-period' + str(period) + 'seconds-scale' + str(scale) + 'volts.txt'
np.savetxt(filename, measure, fmt='%d')

time = np.asarray(list(range(0, len(measure)))) * period

plt.plot(time, measure * scale)
plt.show()