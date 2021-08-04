import numpy as np
import matplotlib.pyplot as plt
import time
import imageio

pic = imageio.imread('White_StripesSpectr.png')

plt.figure(figsize = (5,5))
pic = pic[290:460, 450:560, :]
plt.imshow(pic)

height = pic.shape [0]
width = pic.shape [1]

print(height, width)

gray = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114]) 
gray = gray(pic) 

plt.figure (figsize = (5,5))   
plt.imshow (gray) 
        
plt.show()    

for x in range (height):
    for y in range (width):
        
        r = pic[x, y, 0] 
        g = pic[x, y, 1] 
        b = pic[x, y, 2] 
        sr = (r + g + b) // 3
        
        pic[x, y, :] = sr

print(pic)
plt.imshow(pic)        
plt.show()

