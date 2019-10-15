  
import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import statistics
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

print("Zeroing IMU")
imu.IMURead()
angleSum = 0
for i in range(0, 50):
    print(i)
    
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
    angleSum  += fusionPose[2] 
    print(fusionPose[2])
    #angleSum += math.atan2(compass[1], compass[0])

zeroAngle = angleSum/50

yawList = []
for i in range(0, 10):
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
    yawList.append(fusionPose[2])


while True:
  if imu.IMURead():

    button_pressed = not GPIO.input(23)
    if button_pressed:
        print("Button Pressed")
    # x, y, z = imu.getFusionData()
    # print("%f %f %f" % (x,y,z))
    data = imu.getIMUData()
    #print(data)
    #print("\n\n")
    fusionPose = data["fusionPose"]
    timestamp = data["timestamp"]
    print("time: " + str(timestamp))
    print("yaw Raw: %f" % fusionPose[2])

    yawList.pop(0)
    yawList.append(fusionPose[2])

    yawAvg = statistics.mean(yawList)
    print("Avg Yaw: " + str(yawAvg))

    print("\n")

    #print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
        #math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
    time.sleep(poll_interval*1.0/1000.0)
    #time.sleep(0.25)