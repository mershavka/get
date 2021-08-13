import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read

# Load and cut image
dir = 'C:/Users/ksyurko/Desktop/Repositories/get/12-spectr/DATA/'

# Soft files by last change
files = os.listdir(dir + 'newDATAspectr/')

# for j in range(len(files)):
#     for i in range (len(files)-1):
#         if os.stat(dir+ 'newDATAspectr/' + files[i+1]).st_mtime < os.stat(dir + 'newDATAspectr/'+ files[i]).st_mtime:
#             a = files[i+1]
#             files[i+1] = files[i]
#             files[i] = a  
# print(files)

files[0] = 'White_FullSpectr.png'
files[1] = 'Red_FullSpectr.png'
files[2] = 'Orange_FullSpectr.png'
files[3] = 'Yellow_FullSpectr.png'
files[4] = 'Lightgreen_FullSpectr.png'
files[5] = 'Green_FullSpectr.png'
files[6] = 'Blue_FullSpectr.png'
files[7] = 'darkBlue_FullSpectr.png'
files[8] = 'Crimson_FullSpectr.png'
print (files)