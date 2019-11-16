import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('training/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(1) # wait 5 minutes