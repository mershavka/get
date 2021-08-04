import numpy as np
import matplotlib.pyplot as plt
import time
import imageio

pic = imageio.imread('White_StripesSpectr.png')

pic = pic[290:460, 450:560, :]

height = pic.shape [0]
width = pic.shape [1]
print(height, width)

gray = lambda rgb: np.dot(rgb [..., :3], [0.299, 0.587, 0.114]) 
gray = gray(pic)    

intense = 0
for x in range (width):
# for x in range (height):
    for y in range (height):
    # for y in range (width):
        if gray[y, x] > 3:
            intense += gray[y, x] 
            print (x, ' ', y, ' ', intense)

plt.figure (figsize = (5,5))   
plt.imshow (gray, cmap = plt.get_cmap(name = 'gray')) 

mercury = [576.96, 546.074, 435.83]
picture = [136, 91, 21]

plt.scatter(mercury, picture)

# plt.figure (figsize = (5,5))   
# plt.imshow (pic)
        
plt.show()