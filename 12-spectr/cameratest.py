from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
camera.rotation = 180
time.sleep(1)
camera.capture('/home/pi/Repositories/get/12-spectr/DATA/newDATAspectr/White_StripesSpectr.png')
print('Done!')
