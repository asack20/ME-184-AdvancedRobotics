# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:38:04 2019

@author: Andrew
"""

from edge_detection import detectEdge
import numpy as np
from adafruit_servokit import ServoKit
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
open_button = 23
closed_button = 24 

kit = ServoKit(channels=16) #specify model being used (16 port version)

TL = kit.servo[0];
TR = kit.servo[1];

BL = kit.servo[2];
BR = kit.servo[3];

CL = kit.continuous_servo[4];
CR = kit.continuous_servo[5];

def open_top_gripper():
    TL.angle = 150
    TR.angle = 0
    
    return 0

def close_top_gripper():
    #dist = detectEdge();
    TL.angle = 0
    TR.angle = 180
    
    return 0

def open_bottom_gripper():
    BL.angle = 150
    BR.angle = 0
    
    return 0

def close_bottom_gripper():
    #dist = detectEdge();
    BL.angle = 0
    BR.angle = 180
    
    return 0

def expand():
    button_pressed = not GPIO.input(open_button)
    while not button_pressed:
        CR.throttle = 0.5
        CL.throttle = 0.5
        button_pressed = not GPIO.input(open_button)
    
    CR.throttle = 0
    CL.throttle = 0
        
    return 0

def contract():
    button_pressed = not GPIO.input(closed_button)
    while not button_pressed:
        CR.throttle = -0.5
        CL.throttle = -0.5
        button_pressed = not GPIO.input(closed_button)
    
    CR.throttle = 0
    CL.throttle = 0
        
    return 0

def zero_motion():
    CR.throttle = 0
    CL.throttle = 0

    open_bottom_gripper()
    open_top_gripper()

    return 0

def climb_move():
    close_top_gripper()
    time.sleep(2)
    open_bottom_gripper()
    time.sleep(2)
    contract()
    time.sleep(2)
    close_bottom_gripper()
    time.sleep(2)
    open_top_gripper()
    time.sleep(2)
    expand()
    time.sleep(2)
    close_top_gripper()
    time.sleep(2)

    return 0

##########################################
# Script #################################
##########################################

print("Program Started")

keep_going = True

print("Zeroing Motion")
zero_motion()
time.sleep(2)

while keep_going:
    command = ''
    command = input('"g" to go, "s" to stop\n')
    if command == 'g':
        print("Climbing Up")
        climb_move()

    elif command == 's':
        print("Stopping")
        keep_going = false
        zero_motion()
        time.sleep(2)
    else:
        print("Invalid Command")

