import time
import board, digitalio, busio
from adafruit_servokit import ServoKit

import RPi.GPIO as GPIO
import picamera
import numpy as np
import matplotlib.pyplot as plt
import imageio


with picamera.PiCamera() as camera:
	output = np.empty((720, 1280, 3), dtype=np.uint8)
	camera.capture(output, 'rgb')

plt.figure()
plt.imshow(output)
plt.show()