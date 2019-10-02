import time
#from machine import I2C, Pin
from mpu9250 import MPU9250

imu = MPU9250('X')
while True:
    print(imu.accel.xyz)
    print(imu.gyro.xyz)
    print(imu.mag.xyz)
    print(imu.temperature)
    print(imu.accel.z)
    time.sleep(1)