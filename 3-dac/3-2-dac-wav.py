import RPi.GPIO as GPIO
from time import sleep
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

samplerate, data = wavfile.read('3-dac/SOUND.WAV', True)
print(f"number of dimensions = {data.ndim}")
print(f"array size (n*m) = {data.shape}")
print(f"number of channels = {data.shape[1]}")
print(f"sample rate = {samplerate}")
print(f"data type = {data.dtype}")

length = data.shape[0] / samplerate
print(f"wav duration in seconds = {length}")

maxInt16Value = 2**15 + 1
# import matplotlib.pyplot as plt
# import numpy as np
# time = np.linspace(0., length, data.shape[0])
# plt.plot(time, data[:, 0], label="Left channel")
# plt.plot(time, data[:, 1], label="Right channel")
# plt.legend()
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude")
# plt.show()

left = data[:, 0]
leftUp = (left / maxInt16Value + 1) / 2
print('leftUp',min(leftUp), max(leftUp))
signal = (leftUp * 255).astype(int)

print(signal, min(signal), max(signal))

try:
    for x in signal:
        mask = num2dac(x)
        sleep(0)
        sleep(0)
        sleep(0)
        sleep(0)
        sleep(0)

except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
GPIO.cleanup()
print('GPIO cleanup completed')