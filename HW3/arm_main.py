#Garret Sampel and Andrew Sack
#ME184 - Robotics: HW#3
#10/2/19

from time import sleep    
import numpy as np
import math as m
import sys #for command line arguments
from adafruit_servokit import ServoKit  #uses servo shield api to simplify PWM controll of servos
kit = ServoKit(channels=16) #specify model being used (16 port version)

arm1 = kit.servo[0];
arm2 = kit.servo[1];
pen = kit.servo[2];

#Parameters
l1 = 6.48; #inches
l2 = 6.48; #inches

# Verify command line input
filename = sys.argv[1];
if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments")

###########################################
# File Input

# initalize lists as empty
x_pos_temp = []
y_pos_temp = []
isWrite_temp = []

print('Importing coordinates from ' + filename + '...', end='')

# read in data from file
with open(filename, 'r') as f:
    data = f.readlines()

size = len(data)

# for each line of file (element in data)
for i in range(0, size):
    line = data[i].split('\t'); # split line up by tabs
    x_pos_temp.append(float(line[0])) 
    y_pos_temp.append(float(line[1]))
    isWrite_temp.append(bool(int(line[2])))
# end for

x_in = np.array(x_pos_temp)
y_in = np.array(y_pos_temp)
write_In = np.array(isWrite_temp)

print('done')

################################################
# Interpolate betwwen points
print('Interpolating more coordinates...', end='')
n_steps = 20

for i in range(0, len(x_in)-1):
    x_interp = np.linspace(x_in[i],x_in[i+1], n_steps)
    y_interp = np.linspace(y_in[i],y_in[i+1], n_steps)
    write_interp = np.full(x_interp.size, write_In[i+1])
    if i == 0:
        x_pos = x_interp
        y_pos = y_interp
        isWrite = write_interp
    else:
        x_pos = np.concatenate((x_pos, x_interp), axis=None)
        y_pos = np.concatenate((y_pos, y_interp), axis=None)
        isWrite = np.concatenate((isWrite, write_interp), axis=None)

print('done')

##############################################
# Motion

# Move to zero position
print('Initializing arm postion...', end='')
prev_1 = 90
prev_2 = 90
prev_3 = 0
arm1.angle = prev_1
arm2.angle = prev_2
pen.angle = prev_3
sleep(3)
print('done')


# Run through points
print('Running motion...')
for i in range(0, len(x_pos)):
    # Inverse Kinemetics Calculations
    cos_2 = (x_pos[i]**2 + y_pos[i]**2 - l1**2 - l2**2)/(2*l1*l2)
    sin_2 = m.sqrt(1 - cos_2**2)
    theta_2 = m.degrees(m.atan2(sin_2,cos_2))
    theta_1 = m.degrees(m.atan2(y_pos[i],x_pos[i]) - m.atan2(l2*sin_2,l1+l2*cos_2))
        
    theta_3 = 90*isWrite[i]
    
    # Print to Command Line
    if True:    
        print('Step: ' + str(i))
        print('\t X Pos: '+ str(x_pos[i]))
        print('\t Y Pos: '+ str(y_pos[i]))
        print('\t Arm 1: '+ str(theta_1) + '\t' + str(theta_1%180))
        print('\t Arm 2: '+ str(theta_2) + '\t' +str(theta_2%180))
        print('\t Pen: '+ str(isWrite[i]))

    # Actuate Pen
    if (theta_3 != prev_3):
        pen.angle = theta_3
        sleep(1)  

    # Command servos to move
    arm1.angle = theta_1 % 180
    arm2.angle = (theta_2)  % 180

    prev_1 = theta_1
    prev_2 = theta_2
    prev_3 = theta_3
    
    sleep(0.1) # sleep 0.1 sec between moves

print('done')