import RPi.GPIO as GPIO
from time import sleep

from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def num2dac(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(dac[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

samplerate, data = wavfile.read('C:/Repositories/Education/get/3-dac/ZOOM0001_LR.WAV')
print(f"number of channels = {data.shape[1]}")

length = data.shape[0] / samplerate
print(f"length = {length}s")

import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

left = data[:, 0]
leftUp = left + min(left) * (-1)
leftNorm = leftUp / max(leftUp)

signal = (leftNorm * 255).astype(int)

print(signal, min(signal), max(signal))

try:
    while True:
      value = int(input('Enter value (-1 to exit) > '))
      
      if value < 0:
          break

      mask = num2dac(value)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')