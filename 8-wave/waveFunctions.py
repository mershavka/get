import RPi.GPIO as GPIO
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
button = 22


def initGPIOwave():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds + dac, GPIO.OUT)
    GPIO.setup(troykaVoltage, GPIO.OUT)
    GPIO.setup(comparator, GPIO.IN)
    GPIO.setup(button, GPIO.IN)

    GPIO.output(troykaVoltage, 1)


def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])


def adc2():
    timeout = 0.001
    value = 128
    delta = 128

    for i in range(8):
        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1
        num = delta * direction / 2
        value = int(value + num)
        delta = delta / 2

    return value


def measure(duration): 
    DATE = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
    data = []
    value = 0
    
    start = time.time()
    
    while time.time() - start <= duration:
        value = adc2()
        data.append(value)
        
    return data


def deinitGPIOwave():
    GPIO.output(troykaVoltage, 0)
    GPIO.output(leds + dac, 0)
    GPIO.cleanup()


def softFiles(files):
    for j in range(len(files)):

        for i in range (len(files)-1):

            if os.stat(dir + files[i+1]).st_mtime < os.stat(dir + files[i]).st_mtime:
                a = files[i+1]
                files[i+1] = files[i]
                files[i] = a
    return files


def polynom(measure, levels, degree):
    polyK = np.polyfit(measure, levels, degree) # коэф-ы полинома
    polynom = np.poly1d(polyK) # полином
    print(polynom)

    yvals = np.polyval(polynom, measure)

    return yvals


def polynomPlot(x, y, yvals, degree):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости отсчетов АЦП от уровня воды. ', xlabel = 'Уровень воды, мм', ylabel = 'Отсчеты АЦП')
    ax.legend()

    ax.scatter(x, y, label = 'Точки соответствия отсчетов АЦП уровням воды')
    ax.plot(yvals, y, label = 'Подобранный полином {} степени'.format(degree))

    plt.show()

    fig.savefig('/home/pi/Repositories/get/8-wave/8-wave-plots/WaveCalibration.png')
    

def wavePlot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости уровня воды от времени. ', xlabel = 'Время, с', ylabel = 'Уровень воды, мм')

    box = {'facecolor':'white', 'edgecolor':'black', 'boxstyle':'round'}
    ax.text(13, 107, 'Cкорость распространения волны по полученным данным {} \n Теоретическая скорость распространения волны {}'.format(1, 2), bbox = box, fontsize = 7)
    ax.legend()

    ax.plot(data)

    plt.show()

    fig.savefig('/home/pi/Repositories/get/8-wave/8-wave-plots/FinalWave.png')


def calibrationPlots(measure, level):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости отсчетов АЦП от времени при калибровке', xlabel = 'Время, с', ylabel = 'Отсчеты АЦП')
    ax.legend()

    ax.plot(measure)

    fig.savefig('/home/pi/Repositories/get/8-wave/8-wave-plots/calibrationPlot_{}.png'.format(level))