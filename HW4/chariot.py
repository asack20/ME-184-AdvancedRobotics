import bluetooth
from adafruit_servokit import ServoKit  #uses servo shield api to simplify PWM controll of servos
import time

# Define Servos globally
kit = ServoKit(channels=16) #specify model being used (16 port version)
drive = kit.continuous_servo[0];
turn = kit.servo[1];

def receiveCommands():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print("Accepted connection from " + str(address))
  
  isStop = False
  while not isStop:
    raw_data = client_sock.recv(1024)
    data = raw_data.decode("utf-8") 
    print("Recieved: " + data)
    if data.isdigit():
      val = int(data)
      if val == 999:
        print("Recieved Stop Command. Ending Program")
        isStop = True

      elif val == 0:
        print("Stopping Chariot")
        drive.throttle = 0

      elif val == 1:
        print("Driving Straight")
        drive.throttle = 1
        turn.angle = 90
      elif val == 2:
        print("Driving Left")
        drive.throttle = 1
        turn.angle = 60
      elif val == 3:
        print("Driving Right")
        drive.throttle = 1
        turn.angle = 120
      else:
        print("Revieved Unknown Integer Command")

    else:
      print("Recieved Non-Integer Command")

    


  
  client_sock.close()
  server_sock.close()


def main(args):
  print("Running Chariot code")
  drive.throttle = 0 # zero servos
  turn.angle = 90

  receiveCommands() # listen to commands from controller

  turn.angle = 90 # zero servos 
  drive.throttle = 0
  time.sleep(1) # so servos have time to move
  print("Program Done") 
  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

