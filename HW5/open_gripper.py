import time
import board, digitalio, busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


print("Opening Gripper")
kit.servo[0].angle = 0
time.sleep(2000)

