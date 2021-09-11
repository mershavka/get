import time

import numpy as np
import matplotlib.pyplot as plt
import imageio

import os
from os import read
import pathlib

def loadData(dir):
    files = os.listdir(dir)
    print(files)

    colors = []

    for i in range (len(files)):
        colors.append(imageio.imread(dir + files[i]))

    return colors


def cutpic(picture, dots):
    picture = picture[dots[0]:dots[1], dots[2]:dots[3], :]

    return picture


def polynom(stripes, dots, degree):
    mercury = [576.96, 546.074, 435.83]

    polyK = np.polyfit(stripes, mercury, degree) # коэф-ы полинома
    polynom = np.poly1d(polyK) # полином
    print(polynom)

    yvals = np.polyval(polynom, stripes)
    mercurySpectr = np.polyval(polynom, np.linspace(1, dots[1] - dots[0], dots[1] - dots[0])) # Ox for all plots in wavelengths

    data = [yvals, mercurySpectr]

    return  data


def intensities(colors, dots):
    intensities = []

    for i in range (len(colors)):
        intensity = []

        for y in range (dots[1]-dots[0]):
            oneStripeIntence = 0

            for x in range (dots[3]-dots[2]):
                    
                if sum(colors[i][y, x, :]) > 0:
                    oneStripeIntence += sum(colors[i][y, x, :])

            oneStripeIntence = int( oneStripeIntence/(3*(dots[3]-dots[2]) ))   
            intensity.append(oneStripeIntence)
        intensities.append(intensity)
    
    return intensities


def albedoes(intensities, num):

    albedoes = []

    for i in range (len(intensities)):
        albedo = []

        for k in range (len(intensities[i])):
            albedo.append(intensities[i][k]/intensities[num][k])
        
        albedoes.append(albedo)

    return albedoes


def polynomPlot(xScatter, stripes, degree, dir):
    mercury = [576.96, 546.074, 435.83]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'Зависимость длины волны от номера пикселя (по высоте)', xlabel = 'Номер пикселя', ylabel = 'Длина волны, нм', label = '')

    ax.scatter(stripes, mercury, label = 'Точки соответствия номеров пикселей длинам волн')
    ax.plot(stripes, xScatter, label = 'Подобранный полином {} степени'.format(degree))
    ax.legend(loc=1, bbox_to_anchor=(1, 0.15), prop={'size': 9})

    fig.savefig(dir + 'polynom.png')
    plt.show()


def intensitiesPlot(intensities, wavelength, dir):
    dir1  = 'C:/Users/User/Desktop/Repositories/get/12-spectr/DATA/spectr_photos/'
    rainbow = os.listdir(dir1)
    for i in range(len(rainbow)):
        rainbow[i] = rainbow[i][:-4]
    print(rainbow)

    fig = plt.figure()
    ax = fig.add_subplot(111)           
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = '', xlabel = 'Длина волны, нм', ylabel = 'Интенсивность')
    
    for i in range(len(intensities)):
        ax.plot(wavelength, intensities[i], label = rainbow[i], color = rainbow[i])
        ax.legend()

    plt.show()
    fig.savefig(dir + 'intensitiesPlot.png')


def albedoesPlot(albedoes, wavelength, dir):

    dir1  = 'C:/Users/User/Desktop/Repositories/get/12-spectr/DATA/spectr_photos/'
    rainbow = os.listdir(dir1)
    for i in range(len(rainbow)):
        rainbow[i] = rainbow[i][:-4]

    fig = plt.figure()
    ax = fig.add_subplot(111)           
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости альбедо от длины волны', xlabel = 'Длина волны, нм', ylabel = 'Истиное альбедо')
    
    for i in range(len(albedoes)):
        ax.plot(wavelength, albedoes[i], label = rainbow[i], color = rainbow[i])
        ax.legend()

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)           
        ax1.grid(color = 'gray', linestyle = ':')
        ax1.set(title = 'График зависимости альбедо от длины волны', xlabel = 'Длина волны, нм', ylabel = 'Истиное альбедо')
        ax1.plot(wavelength, albedoes[i], label = rainbow[i], color = rainbow[i])
        ax1.legend()

        fig.savefig(dir + 'albedoPlot{}.png'.format(i))


    plt.show()
    fig.savefig(dir + 'albedoPlot.png')