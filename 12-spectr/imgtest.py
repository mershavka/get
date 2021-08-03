import numpy as np
import matplotlib.pyplot as plt
import time
import imageio

pic = imageio.imread('omg.png')

plt.figure(figsize = (5,5))

plt.imshow(pic)

print ('Тип изображения:', type (pic)) 
print ('Форма изображения: {}'.format(pic.shape)) 
print ('Image Hight {}'.format(pic.shape [0])) 
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

pic [700:750, :, 0] = 0 # полная интенсивность для канала R этого пикселя 

plt.title ('R канал') 
plt.ylabel ('Высота {}'.format(pic.shape [0])) 
plt.xlabel ('Ширина {}'.format(pic.shape [1])) 

height = pic.shape [0]
width = pic.shape [1]

gray = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114]) 
gray = gray(pic) 

plt.figure (figsize = (5,5))   
plt.imshow (gray, cmap = plt.get_cmap(name = 'gray')) 
        
plt.show()    

# for x in range (height):
#     for y in range (width):
        
#         r = pic[x, y, 0] 
#         g = pic[x, y, 1] 
#         b = pic[x, y, 2] 
#         sr = (r + g + b) // 3
        
#         pic[x, y, :] = sr

# print(pic)
# plt.imshow(pic)        
# plt.show()

