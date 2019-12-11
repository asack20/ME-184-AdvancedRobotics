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

# End Stop button setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
closed_button = 23 

kit = ServoKit(channels=16) #specify model being used (16 port version)

# Define Servos
TL = kit.servo[8];
TR = kit.servo[9];

BL = kit.servo[4];
BR = kit.servo[5];

CL = kit.continuous_servo[0];
CR = kit.continuous_servo[1];

tail = kit.servo[7];

################################
# Functions: ###################
################################

def open_top_gripper():
    TL.angle = 150
    TR.angle = 30
    
    return 0

def close_top_gripper():
    dist = detectEdge();
    TL.angle = 0
    TR.angle = 180
    
    return 0

def open_bottom_gripper():
    BL.angle = 150
    BR.angle = 30
    tail.angle = 90
    
    return 0

def close_bottom_gripper():
    BL.angle = 0
    BR.angle = 180
    tail.angle = 180

    return 0

def expand():
    CR.throttle = -1
    CL.throttle = -1
    
    time.sleep(30) # Move for 30 seconds
    
    CR.throttle = 0
    CL.throttle = 0
        
    return 0

def contract():
    # Close until end stop is reached
    button_pressed = not GPIO.input(closed_button)
    while not button_pressed:
        CR.throttle = 1
        CL.throttle = 1
        button_pressed = not GPIO.input(closed_button)
    
    CR.throttle = 0
    CL.throttle = 0
        
    return 0

# Stops continuous servos and opens claws as safe reset position
def zero_motion():
    CR.throttle = 0
    CL.throttle = 0

    open_bottom_gripper()
    time.sleep(2)
    open_top_gripper()
    time.sleep(2)

    return 0

# Main climbing motion of one step
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
zero_motion() # Zero motion at beginning
time.sleep(2)

while keep_going: # Climb until stop command given
    command = ''
    command = input('"g" to go, "s" to stop\n')
    if command == 'g': # perform a climb step
        print("Climbing Up")
        climb_move()

    elif command == 's': # Reset position and quit program
        print("Stopping")
        keep_going = False
        zero_motion()
        time.sleep(2)
    else:
        print("Invalid Command")

