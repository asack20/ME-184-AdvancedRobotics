import time
import board, digitalio, busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def main(args):
    print("Closing Gripper")
    kit.servo[0].angle = 180
    time.sleep(2000)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
