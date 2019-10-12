import bluetooth

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print("Accepted connection from " + str(address))
  
  data = "0"
  while data != "999":
    raw_data = client_sock.recv(1024)
    data = raw_data[2:len(raw_data)]
    print("received [%s]" % raw_data)
    print(data)

  
  client_sock.close()
  server_sock.close()


def main(args):
  print("Running Bluetooth recieve code")
  receiveMessages()
      #time.sleep(2)
  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

