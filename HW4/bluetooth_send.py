import bluetooth
import time

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
	mac = "B8:27:EB:64:6F:44"
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

	for i in range(0, 10):
		print("Sending: " + str(i))
		sendMessageTo(sock, str(i))
		time.sleep(0.1)
	
	sock.send(str(999))
	sock.close()

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
