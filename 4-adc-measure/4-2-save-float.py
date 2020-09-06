import numpy as np
import matplotlib.pyplot as plt

measure = np.random.randint(255, size = 1000)
period = 0.001
scale = 0.013

filename = '4-adc-measure/data.csv'

time = np.asarray(list(range(0, len(measure)))) * period
voltage = np.asarray(measure) * scale
data = np.dstack((time, voltage))

np.savetxt(filename, data[0], fmt='%.3f', delimiter=',', header='time-s,voltage-v', comments='')

plt.plot(time, voltage)
plt.show()