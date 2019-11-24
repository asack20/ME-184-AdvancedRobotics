import time
import board, digitalio, busio
from adafruit_servokit import ServoKit

import time

import RPi.GPIO as GPIO
import picamera
import numpy as np
import matplotlib.pyplot as plt
import imageio


LEDPIN = 21
FORCEPIN = 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT) #LEDS to GPIO21



def led_on():
	GPIO.output(LEDPIN, GPIO.HIGH)

def led_off():
	GPIO.output(LEDPIN, GPIO.LOW)


def capture_frame():
	with picamera.PiCamera() as camera:
		output = np.empty((720, 1280, 3), dtype=np.uint8)
		camera.capture(output, 'rgb')
	return output

def plot_frame(arr):
    plt.figure()
    plt.imshow(arr)
    plt.show()


for i in range(0,3):
	led_on()
	time.sleep(3)
	led_off()
	time.sleep(3)

# for i in range(0,3):
# 	out = capture_frame()
# 	plot_frame(out)
# 	time.sleep(2)

plt.show()
GPIO.cleanup()