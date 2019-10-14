import bluetooth
import time
import getopt
sys.path.append('.')
import RTIMU
import os.path
import math


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
		if imu.IMURead():
			data = imu.getIMUData()
			timestamp = data["timestamp"]
			compass = data["compass"]
			print("time: " + str(timestamp))
			print("x: %f y: %f z: %f" % (compass[0],compass[1],compass[2]))
			print("\n")

		sock.send(str(compass))
		time.sleep(poll_interval*1.0/1000.0)
	
	sock.send(str(999))
	sock.close()

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
