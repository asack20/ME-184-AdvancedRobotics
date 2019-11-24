# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:03:16 2019

@author: Andrew
"""
import imageio
import numpy as np

import matplotlib.pyplot as plt
import cv2


def color_dist(im):
    im_color = np.mean(im, axis = (0,1))
    
    rgb_ref = np.array([[137, 131, 114],[104,90,74],[106,122,125],[117, 141, 153],[123,123,117]])
    
    cDist = np.zeros((5))
    for i in range(0,5):
        cDist[i] = np.sqrt(np.square(im_color[0] - rgb_ref[i,0]) +  np.square(im_color[1] - rgb_ref[i,1]) + np.square(im_color[2] - rgb_ref[i,2])   )
       
    return cDist

cName = ['wood','carpet','brick','metal','tree']

mins = np.zeros((30))
minInds = np.zeros((30))
for i in range(1, 31):    
    im = imageio.imread('training/tree_Template/patch%03d.jpg'%i)
    #print('Image #%d' %i)
    cDist = color_dist(im)
    mins[i-1] = np.min(cDist)
    minInds[i-1] = np.argmin(cDist)  
    #print(cName[int(minInds[i-1])])    
    
print('Wood: %d' % np.sum(minInds == 0))
print('Carpet: %d' % np.sum(minInds == 1))
print('Brick: %d' % np.sum(minInds == 2))
print('Metal: %d' % np.sum(minInds == 3))
print('Tree: %d' % np.sum(minInds == 4))
