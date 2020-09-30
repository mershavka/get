import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def num2dac(value):
    mask = bin(value)[2:].zfill(bits)

    for i in range(0, len(mask)):
        GPIO.output(dac[i], GPIO.HIGH if mask[i] == '1' else GPIO.LOW)

t = 3
f = 440*8
sf = 48000

time = np.linspace(0, t, t * sf)
signal = (((np.sin(2 * np.pi * f * time) + 1) / 2) * 255).astype(int)

print(signal)

# plt.plot(time, signal)
# plt.show()

try:
    for x in signal:
      mask = num2dac(x)
      sleep(1/(sf/2))

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')