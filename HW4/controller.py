import bluetooth
import time
import getopt
import sys
sys.path.append('.')
import RTIMU
import os.path
import math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23


def connectTo(targetBluetoothMacAddress):
  port = 1
  sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("Connected from: " + targetBluetoothMacAddress)
  
  return sock



def sendMessageTo(sock, message):
  sock.send(message)
  return

def main(args):
	print("Running IMU Controller code")
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

	# Callibrate Zero
	print("Zeroing IMU")
	imu.IMURead()
	angleSum = 0
	for i in range(0, 50):
		data = imu.getIMUData()
		fusionPose = data["fusionPose"]
		angleSum = angleSum + fusionPose[2] 

	zeroAngle = angleSum/50
	print("Done Zeroing IMU")
	print("Zero Angle: " + str(zeroAngle))

	mac = "B8:27:EB:80:EB:FD"
	isConnected = False

	while not isConnected:
	    print("Attempting connection to: " + str(mac))
	    try:
	    	sock = connectTo(mac)
	    	isConnected = True
	    except:
	    	print("Could not connect. Will try again in 2 seconds")
	    	isConnected = False
	    	time.sleep(2)
	
	print("Connected to: " + mac + "\n")

	while True:
		message = "0"
		button_pressed = not GPIO.input(23)
		if button_pressed and imu.IMURead():
			print('Button Pressed...')
			data = imu.getIMUData()
			fusionPose = data["fusionPose"]
			print("Yaw Raw: %f" % fusionPose[2])
			angle = fusionPose[2] - zeroAngle
			print("Yaw Zeroed: %f" % angle)
			if abs(angle) <= 1:
				message = "1"
			elif angle > 1:
				message = "3" # Right
			elif angle < -1:
				message = "2" # Left
			

		sock.send(message)
		time.sleep(poll_interval*1.0/1000.0)
	
	sock.send(str(999))
	sock.close()
	GPIO.cleanup()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
