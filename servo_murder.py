from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

for i in range(16):
	kit.continuous_servo[i].throttle = 0