import numpy as np
import matplotlib.pyplot as plt
import imageio

import time
import pathlib

import os
from os import read

import spectrFunctions as func

dir = 'C:/Users/User/Desktop/Repositories/get/12-spectr/DATA/spectr_photos/'

rainbow = os.listdir(dir)
print(rainbow)
for i in range(len(rainbow)):
    rainbow[i] = rainbow[i][:-4]
 
print(rainbow)