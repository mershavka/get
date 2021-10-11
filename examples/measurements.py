import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

leds = [21, 20, 16, 12, 7, 8, 25, 23]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4
troykaVoltage = [17]
 
bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels
timeout = 0.001
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)
  
def num2pins(pins, value):
    if not type(pins) is list:
        return
    if type(value) is list:
        GPIO.output(pins, value)
    elif type(value) is int:
        GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])
  
def adc():
    
    value = [0] * 8
    result = 0
    
    for i in range(8):
        value[i] = 1
        GPIO.output(dac, value)
        time.sleep(timeout)
        value[i] = GPIO.input(comparator)
        result += value[i] * 2**(bits - 1 - i)
     
    return result
  
try: 
    measured_data = []
    value = 0
      
    start = time.time()

    GPIO.output(troykaVoltage, 1)
      
    while value <= 245:
        value = adc()
        GPIO.output(leds, value)
        measured_data.append(value)
  
    GPIO.output(troykaVoltage, 0)
  
    while value > 1:
        value = adc()
        GPIO.output(leds, value)
        measured_data.append(value)
  
    finish = time.time()
  
    totalTime = finish - start
    measurePeriod = totalTime / (len(measured_data)-1)
    samplingFrequency = int(1 / measurePeriod)
  
    print("Total measure time: {:.2f} s, measure period: {:.3f} ms, sampling frequency: {:d} Hz".format(totalTime, measurePeriod, samplingFrequency))
    print("Voltage step: {:.3f} V".format(dV))
  
    plt.plot(measured_data)
    plt.show()
  
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(str(item) for item in measured_data))
  
finally:
    GPIO.output(leds + dac, 0)
    GPIO.cleanup()
    print('GPIO cleanup completed.')
