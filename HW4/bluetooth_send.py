import bluetooth
import time

def sendMessageTo(targetBluetoothMacAddress, message):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send(message)
  sock.close()


def main(args):
	mac = "B8:27:EB:64:6F:44"
	message = "testing testing"

	while True:
	    print("Test")
	    try:
	    	sendMessageTo(mac, message)
	    time.sleep(2)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
