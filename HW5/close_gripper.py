import time
import board, digitalio, busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


print("Closing Gripper")
kit.servo[0].angle = 180
time.sleep(2000)
