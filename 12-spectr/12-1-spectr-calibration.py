import numpy as np
import matplotlib.pyplot as plt
import time
import imageio
from io import BytesIO

# Load and cut image
dir = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/'

pic = imageio.imread(dir + 'StripesSpectr/White_StripesSpectr.png')
pic = pic[310:443, 468:540, :]


# Make monochrome
gray = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114]) 
gray = gray(pic)    

height = pic.shape [0]
width = pic.shape [1]
print(height, width)


# Mercury calibration
picture = [576.96, 546.074, 435.83]
mercury = [136, 91, 21]


# Polynomial selection
degree = 2
polyK = np.polyfit(picture, mercury, degree) # коэф-ы полинома
polynom = np.poly1d(polyK) # полином
print(polynom)

yvals = np.polyval(polynom, picture)
mercurySpectr = np.polyval(polynom, np.linspace(0, height, height)) 


# Make intervals lists
intervals = [[630, 800], 
            [590, 630], 
            [570, 590], 
            [550, 570], 
            [510, 550], 
            [480, 510], 
            [450, 480], 
            [300, 450]] 

for i in range (len(intervals)):
    xvals = np.polyval(polynom, np.linspace(intervals[i][0], intervals[i][1], intervals[i][1]-intervals[i][0]))
    print(xvals.astype(np.int32))
    np.savetxt(dir + 'interval_{}'.format(i), xvals.astype(np.int32),  fmt='%d')


# Show monochrome image
plt.figure (figsize = (5,5))   
plt.imshow (gray, cmap = plt.get_cmap(name = 'gray'))


# Create calibration plot
figCalib = plt.figure()
ax = figCalib.add_subplot(111)
ax.grid(color = 'gray', linestyle = ':')
ax.set(title = 'Зависимость длины волны от номера пикселя (по высоте)', xlabel = 'Номер пикселя', ylabel = 'Длина волны, нм', label = '')

ax.scatter(picture, mercury, label = 'Точки соответствия номеров пикселей длинам волн')
ax.plot(picture, yvals, label = 'Подобранный полином {} степени'.format(degree))
ax.legend(loc=1, bbox_to_anchor=(1, 0.15), prop={'size': 9})

# Create DATA plot
wavelengthsfig = plt.figure()
wavelengthsax = wavelengthsfig.add_subplot(111)
wavelengthsax.grid(color = 'gray', linestyle = ':')
wavelengthsax.set(title = 'Зависимость длины волны от номера пикселя', xlabel = 'Номер пикселя', ylabel = 'Длина волны, нм')

wavelengthsax.plot(mercurySpectr)
        
plt.show()

# Save plots and mercurySpectr
np.savetxt(dir + '/mercurySpectr.txt', mercurySpectr, fmt='%d')

figCalib.savefig(dir + 'calibrationPlot.png')
wavelengthsfig.savefig(dir + 'mercuryPlot.png')

imageio.imwrite(dir + 'White_StripesSpectr.color.png', pic, format='png')
imageio.imwrite(dir + 'White_StripesSpectr.monochrome.png', gray.astype(np.uint8), format='png')