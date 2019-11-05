import time
import board, digitalio, busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def main(args):
    while True:
        print(time.localtime())
        kit.continuous_servo[0].throttle = 0
        time.sleep(10)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
