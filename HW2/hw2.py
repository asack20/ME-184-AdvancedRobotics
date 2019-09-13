#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hw2.py
#  
#  Copyright 2019  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
import board, digitalio, busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def main(args):
    while True:
        print(time.localtime())
        kit.continuous_servo[0].throttle = 1
        time.sleep(2)
        kit.continuous_servo[0].throttle = 0
        time.sleep(2)
        kit.continuous_servo[0].throttle = -1
        time.sleep(2)
        kit.continuous_servo[0].throttle = 0
        time.sleep(2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
