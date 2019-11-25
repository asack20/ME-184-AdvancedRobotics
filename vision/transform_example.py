# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:03:27 2019

@author: Andrew
"""

# import the necessary packages
from transform import four_point_transform
import numpy as np
import cv2
 
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread('training3/img002.jpg')
pts = np.array([[492, 0],[966,0],[804,720],[589,720]], dtype = "float32")
 
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
 
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)