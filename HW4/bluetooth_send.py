import bluetooth
import time

# def connectTo(targetBluetoothMacAddress):
#   port = 1
#   sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#   sock.connect((targetBluetoothMacAddress, port))
#   sock.send("Connected from: " + targetBluetoothMacAddress)
  
#   return sock



# def sendMessageTo(sock, message):
#   sock.send(message)
#   return sock

def main(args):
	mac = "B8:27:EB:64:6F:44"
	message = "testing testing"
	isConnected = False

	while not isConnected:
	    print("Attempting connection to: " + str(mac))
	    try:
	    	port = 1
	    	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	    	sock.connect((mac, port))
	    	sock.send("Connected from: " + mac)
	    	isConnected = True
	    except:
	    	print("Could not connect. Will try again in 2 seconds")
	    	isConnected = False
	    	time.sleep(2)
	print("Connected to: " + mac + "\n")

	for i in range(0, 10):
		print("Sending: " + str(i))
		sock.send(str(i))
		time.sleep(5)
	sock.close()

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
