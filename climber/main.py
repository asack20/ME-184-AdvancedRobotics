# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:38:04 2019

@author: Andrew
"""

from edge_detection import detectEdge
import numpy as np
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16) #specify model being used (16 port version)

left = kit.servo[0];
right = kit.servo[1];

def open_gripper():
    left.angle = 150
    right.angle = 0
    
    return 0

def close_gripper():
    dist = detectEdge();
    left.angle = 0
    right.angle = 180
    
    return 0

while True:
    command = ''
    command = input('"c" to close, "o" to open\n')
    if command == 'c':
        print("Closing Gripper")
        close_gripper()
        time.sleep(2)
    elif command == 'o':
        print("Opening Gripper")
        open_gripper()
        time.sleep(2)
    else:
        print("Invalid Command")

