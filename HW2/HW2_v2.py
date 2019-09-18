#written by Garret Sampel
#ME184 - Robotics: HW#2
#9/13/19

import datetime #allows method of aquiring current time
import time     #allows delays in code
from adafruit_servokit import ServoKit  #uses servo shield api to simplify PWM controll of servos
kit = ServoKit(channels=16) #specify model being used (16 port version)

hourStep = 120/12 #120deg of motion devided evenly over required number of steps
minStep = 120/60
secStep = 120/60

while True:  #infinite loop
    currentDT = datetime.datetime.now() #get current time
    print(str(currentDT)+" "+str(120-currentDT.second*secStep)) #debug line, TODO RM @ turn-in
    #VALUE BETWEEN 0-180 TRUE CENTER = 158 for our servos
    if currentDT.hour>12:
        hours = currentDT.hour-12
    else:
        hours = currentDT.hour
    kit.servo[0].angle = (120-hours*hourStep) #val from 1-24
    kit.servo[1].angle = (120-currentDT.minute*minStep) #val from 1-60
    kit.servo[2].angle = (120-currentDT.second*secStep) #val from 1-60
    time.sleep(1)
