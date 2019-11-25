# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:42:01 2019

@author: Andrew
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

plt.close('all')



gray = cv2.imread('training3/img002.jpg',0)

# Smoothing without removing edges.
gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)

# Applying the canny filter
edges = cv2.Canny(gray, 60, 120)
edges_filtered = cv2.Canny(gray_filtered, 60, 120)

# Stacking the images to print them together for comparison
canny_images = np.hstack((gray, edges, edges_filtered))

# Display the resulting frame
#cv2.imshow('Frame', canny_images)
plt.imshow(canny_images)

#edges = cv.Canny(img, 20,30)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()