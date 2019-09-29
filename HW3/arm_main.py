#Garret Sampel and Andrew Sack
#ME184 - Robotics: HW#3
#10/2/19

from time import sleep    
import numpy as np
import sys #for command line arguments
from adafruit_servokit import ServoKit  #uses servo shield api to simplify PWM controll of servos
kit = ServoKit(channels=16) #specify model being used (16 port version)


#Parameters
l1 = 10; #inches
l2 = 10; #inches


arm1 = kit.servo[0];
arm2 = kit.servo[1];
pen = kit.servo[3]

filename = sys.argv[1];
if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments")


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
    isWrite_temp.append(bool(line[2]))
# end for


x_pos = np.array(x_pos_temp)
y_pos = np.array(y_pos_temp)
isWrite = np.array(isWrite_temp)

print('done')

print('Calculating servo target angles...', end='')

# calculate motor angles from position all in radians
cos_alpha = (np.square(l2) - (np.square(l1) + (np.square(x_pos) + np.square(y_pos))))/(-2*l1*np.sqrt(np.square(x_pos) + np.square(y_pos)))
#print(cos_alpha) 
alpha_calc = np.arctan2(np.sqrt(1 - np.square(cos_alpha)), cos_alpha)
beta_calc = np.arctan2(y_pos, x_pos)

theta_1_r = alpha_calc + beta_calc

cos_theta = ((np.square(x_pos) + np.square(y_pos)) - (np.square(l1) + np.square(l2)))/(-2*l1*l2)
theta_2_r = -np.arctan2(np.sqrt(1 - np.square(cos_theta)),cos_theta)

# target motor position in degrees
theta_1 = np.degrees(theta_1_r)
theta_2 = np.degrees(theta_2_r) 
theta_3 = 90*isWrite

print('done')

print('Initializing arm postion...', end='')
prev_1 = 0
prev_2 = 0
prev_3 = 0
arm1.angle = prev_1
arm2.angle = prev_2
pen.angle = prev_3
sleep(3)
print('done')


print('Running motion...')
for i in range(0, len(theta_1)):
    if True:    
        print('Step: ' + str(i))
        print('\t X Pos: '+ str(x_pos[i]))
        print('\t Y Pos: '+ str(y_pos[i]))
        print('\t Arm 1: '+ str(theta_1[i]))
        print('\t Arm 2: '+ str(theta_2[i]))
        print('\t Pen: '+ str(isWrite[i]))

    if (theta_3[i] != prev_3):
        pen.angle = theta_3[i]
        sleep(0.5)
    
    delta_1 = theta_1[i] - prev_1
    delta_2 = theta_2[i] - prev_2

    delta_max = max(abs(delta_1), abs(delta_2))
    t_sleep = delta_max / 300

    arm1.angle = theta_1[i] % 180
    arm2.angle = theta_2[i] % 180

    prev_1 = theta_1[i]
    prev_2 = theta_2[i]
    prev_3 = theta_3[i]
    
    sleep(t_sleep)

print('done')