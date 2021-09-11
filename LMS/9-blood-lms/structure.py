import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib
import bloodFunctions as func

# Сокращения - LFN - long file name, HC - high calibration, LC - low calibration, MR - measure rest, MF - measure fitness

# Введение значений в переменные
dir = # директория

high = # первая точка калибровки
low = # вторая точка калибровки

# Введение постояннных в переменные (после первого запуска программы)
SP1 = 
tSP1 = 
DP1 = 
tDP1 = 
num1 = 

SP2 = 
tSP2 = 
DP2 = 
tDP2 = 
num2 = 

LFN_HC = '08.07.2021-13.26.03_0.009.txt'
LFN_LC = '08.07.2021-13.26.33_0.009.txt'
LFN_MR = '08.07.2021-13.27.51_0.009.txt'
LFN_MF = '08.07.2021-13.29.18_0.009.txt'

# Загрузка данных файлов в массивы
........

# Присвоение переменным частоты дескритизации из названия файла
delta_HC = float(pathlib.Path(LFN_HC).stem[20:])
delta_LC = float(pathlib.Path(LFN_LC).stem[20:])
delta_MR = float(pathlib.Path(LFN_MR).stem[20:])
delta_MF = float(pathlib.Path(LFN_MF).stem[20:])


# Сглаживание массивов данных
N1 = 20

HC_Smothed = np.convolve(HC, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления калибровки 1

LC_Smothed = np.convolve(LC, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления калибровки 2

MR_Smothed = np.convolve(MR, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления до физ.нагрузки
MR_Smothed1 = MR_Smothed

MF_Smothed = np.convolve(MF, np.ones((N1,))/N1, mode = 'valid') #массив данных для графика давления после физ.нагрузки
MF_Smothed1 = MF_Smothed

# Сглаживание массивов данных для пульса
N2 = 600

for i in range (N2-N1):
    MR_Smothed1 = np.delete(MR_Smothed1, 0)
pulsWave1 = MR_Smothed1 - np.convolve(MR, np.ones((N2,))/N2, mode = 'valid') #массив данных для первой пульсовой волны

for i in range (N2-N1):
    MF_Smothed1 = np.delete(MF_Smothed1, 0)
pulsWave2 = MF_Smothed1 - np.convolve(MF, np.ones((N2,))/N2, mode = 'valid') #массив данных для второй пульсовой волны

# Вычисление среднего значения для каждой калибровки и коэффициента наклона
........

# Создание массивов отсчетов времени (с помощью функции np.linspace)
........

# Вычисление пульса
........

# Создание графиков
........