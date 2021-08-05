import numpy as np
import matplotlib.pyplot as plt
import time
import imageio
from io import BytesIO

# Load and cut image
pic = imageio.imread('/home/pi/Repositories/get/12-spectr/DATA/StripesSpectr/White_StripesSpectr.png')
pic = pic[290:460, 450:560, :]

# Make monochrome
gray = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114]) 
gray = gray(pic)    

# Pixel intensly
height = pic.shape [0]
width = pic.shape [1]
print(height, width)

intense = 0

for x in range (width):
    for y in range (height):

        if gray[y, x] > 3:
            intense += gray[y, x] 
            print (x, ' ', y, ' ', intense) 

# Mercury calibration
mercury = [576.96, 546.074, 435.83]
picture = [136, 91, 21]

# Polynomial selection
degree = 2
polyK = np.polyfit(picture, mercury, degree) # коэф-ы полинома
polynom = np.poly1d(polyK) # полином
print(polynom)

yvals = np.polyval(polynom, picture)
mercurySpectr = np.polyval(polynom, np.linspace(0, height, height)) 

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
np.savetxt('/home/pi/Repositories/get/12-spectr/DATA/mercurySpectr.txt', mercurySpectr, fmt='%d')

figCalib.savefig('/home/pi/Repositories/get/12-spectr/DATA/calibrationPlot.png')
wavelengthsfig.savefig('/home/pi/Repositories/get/12-spectr/DATA/mercuryPlot.png')

imageio.imwrite('/home/pi/Repositories/get/12-spectr/DATA/White_StripesSpectr.color.png', pic, format='png')
imageio.imwrite('/home/pi/Repositories/get/12-spectr/DATA/White_StripesSpectr.monochrome.png', gray.astype(np.uint8), format='png')