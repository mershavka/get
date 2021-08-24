import RPi.GPIO as GPIO
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt



dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4 
troykaVoltage = 17

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])

def adc2():

    timeout = 0.00001
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

def trackingADC():
    
    U = adc3() + 1

    if GPIO.input(comparator) == 0:
        while GPIO.input(comparator) == 0:
            U -= 1
            break

    if  GPIO.input(comparator) == 1:
        while GPIO.input(comparator) == 1:
            U -= 1
            break
    return U 

def adc3():
    mass = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):
        
        # print(mass)
        mass[i] = 1
        GPIO.output(dac, mass)
        time.sleep(0.0000001)

        if GPIO.input(comparator) == 0:
            mass[i] = 0
        

    return mass[0]*2**7 + mass[1]*2**6 + mass[2]*2**5 + mass[3]*2**4 + mass[4]*2**3 + mass[5]*2**2 + mass[6]*2**1 + mass[7]*2**0



try:
    
    now = datetime.datetime.now()
  
    t = 1
    measure = []
    value = 0
    
    start = time.time()

    GPIO.output(troykaVoltage, 1)
    # print(adc3())

    while time.time() - start <= t:
        value = adc3()
        measure.append(value)
    
    np.savetxt('/home/pi/get/4-adc/adcTest/test1.txt', measure, fmt='%d')
    print('Done! Files already saved!')

    # Creating calibration plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(measure)

    plt.show()

finally:
    
    GPIO.cleanup()
    print('GPIO cleanup completed.')