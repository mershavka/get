from picamera import PiCamera
import time

photo = input('Enter color name: ')
lamp = input('if the lamp is mercury, enter "1"\n if lamp is incandescent, enter "2"')
camera = PiCamera()
camera.start_preview()

camera.rotation = 180
time.sleep(1)

camera.capture('/home/pi/Repositories/get/12-spectr/DATA/newDATAspectr/{}_{}.png'.format(photo, lamp))
print('Done! You can enjoy the photo)')