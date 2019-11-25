# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:18:14 2019

@author: Andrew
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:59:55 2019

@author: Andrew
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:18:09 2019

@author: Andrew
"""

#from IPython import get_ipython
#def __reset__(): get_ipython().magic('reset -sf')

import numpy as np
#import imageio
#from convolve_func import basic_conv
from scipy.signal import find_peaks, fftconvolve
from scipy.ndimage.filters import gaussian_filter
import picamera

with picamera.PiCamera() as camera:
	output = np.empty((720, 1280, 3), dtype=np.uint8)
	camera.capture(output, 'rgb')



def detectEdge():
    print("Detecting Edge")
    with picamera.PiCamera() as camera:
        output = np.empty((720, 1280, 3), dtype=np.uint8)
        camera.capture(output, 'rgb')
    print("Took Image")
    
    imPic = np.mean(output, axis=2)

    imBlur = gaussian_filter(imPic, sigma=3)
    imThresh = np.copy(imBlur)
    imThresh[np.logical_and(imThresh > 50, imThresh < 130)] = 0
    
    
    imRaw = imBlur - imThresh
    
    vertSob = [[1,0,-1],[2,0,-2],[1,0,-1]]
    #vertEdge = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
    #totEdge = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    #blur = [[1/16, 1/8, 1/16],[1/8, 1/4, 1/8],[1/16, 1/16,1/8]]
    #sharp = [[0,-1,0],[-1,5,-1],[0,-1,0]]
    
    print("Thresholded Image")
    
    im = fftconvolve(imRaw, vertSob, mode='same')
    
    print("Convolved Image")
    
    n = 80
    im[im < n] = 0
    im[im > n] = n
    
    eRow = im.sum(axis = 0) / 80
    eRow[0:5] = np.zeros((1,5))
    
    peaks, _ = find_peaks(eRow, distance = 250)
    
    sorted_peaks = np.argsort(eRow[peaks])
    if len(peaks) < 2:
        print("No edges found")
        return -1
    
    pk1 = peaks[sorted_peaks[-1]]
    pk2 = peaks[sorted_peaks[-2]]
    
    dist = abs(pk1 - pk2)
    print("Found Edges")
    print(dist)
    
    return dist

while True:
    detectEdge()
