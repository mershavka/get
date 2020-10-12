# Script starts to run right here!
# Yes, script is already running!

################################################################################
# Import modules (prepare script)
################################################################################

import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


################################################################################
# Create variables that will not change in our script ("constants") 
################################################################################

leds = [21, 20, 16, 12, 7, 8, 25, 23]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4
troykaVoltage = 17

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels


################################################################################
# Setup GPIO for this run of the script
################################################################################

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)


################################################################################
# Define functions for this run of the script
################################################################################

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])

def adc():

    value = 0
    up = True

    for i in range(0, bits):
        delta = 2 ** (bits - 1 - i)
        value = value + delta * (1 if up else -1)

        num2pins(dac, value)
        time.sleep(0.0011)

        up = bool(GPIO.input(comparator))

    return value


# Main logic of the script starts only here!

################################################################################
# "Try block" with all your "application" or "user" logic
################################################################################

try:
    # 1. Create variables

    measure = []
    period = 1
    value = 0


    # 2. Fix start time
    
    start = time.time()


    # 3. Charge capacitor
    
    GPIO.output(troykaVoltage, 1)
    
    while value < 248:
        value = adc()
        num2pins(leds, value)
        measure.append(value)


    # 4. Discharge capacitor

    GPIO.output(troykaVoltage, 0)

    while value > 5:
        value = adc()
        num2pins(leds, value)
        measure.append(value)


    # 5. Fix finish time and print time values

    finish = time.time()

    totalTime = finish - start
    measurePeriod = totalTime / len(measure)
    samplingFrequency = int(1 / measurePeriod)

    print("Total measure time: {:.2f} s, measure period: {:.3f} ms, sampling frequency: {:d} Hz".format(totalTime, measurePeriod, samplingFrequency))
    print("Voltage step: {:.3f} V".format(dV))

    # 6. Plot results

    plt.plot(measure)
    plt.show()

    np.savetxt('5-adc-measure/data.txt', measure, fmt='%d')


################################################################################
# "Finally block" with functions that must be execute after script any way
################################################################################

finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')