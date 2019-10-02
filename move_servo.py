import sys #for command line arguments
from adafruit_servokit import ServoKit  #uses servo shield api to simplify PWM controll of servos

kit = ServoKit(channels=16) #specify model being used (16 port version)

arm1 = kit.servo[0];
arm2 = kit.servo[1];
pen = kit.servo[2];


# Verify command line input
servo_num = int(sys.argv[1]);
ang = int(sys.argv[2]);



if len(sys.argv) != 3:
    print("Incorrect number of arguments")
    print("Correct Command is:")
    print("python3 move_servo.py (servo_number) (angle)")
    sys.exit()

kit.servo[servo_num].angle = ang