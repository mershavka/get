import numpy as np
import matplotlib.pyplot as plt
import time
import imageio

pic = imageio.imread('omg.png')


plt.figure(figsize = (5,5))

plt.imshow(pic)

print ('Тип изображения:', type (pic)) 
print ('Форма изображения: {}'.format(pic.shape)) 
print ('Image Hight {}'.format(pic.shape [0 ])) 
print ('Ширина изображения {}'.format(pic.shape [1])) 
print ('Размер изображения {}'.format(pic.ndim))

print ('Размер изображения {}'.format(pic.size)) 
print ('Максимальное значение RGB в этом изображении {}'.format(pic.max())) 
print ('Минимальное значение RGB в этом изображении {}'.format(pic.min ()))

print()

# Определенный пиксель, расположенный в строке: 100; Столбец: 50   
# Значение каждого канала, постепенно R, G, B   
print ('Значение только канала R {}'.format (pic [100, 50, 0])) 
print ('Значение только канала G {} '.format (pic [100, 50, 1])) 
print ('Значение только  B {} '.format (pic [100, 50, 2]))