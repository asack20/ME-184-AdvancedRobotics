# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:18:14 2019

@author: Andrew
"""


import numpy as np
from scipy.signal import find_peaks, fftconvolve
from scipy.ndimage.filters import gaussian_filter
import picamera

# Perform material detection
def closestMaterial(im):
    im_color = np.mean(im, axis = (0,1)) # calc mean color of image
    cName = ['wood','carpet','brick','metal','tree']
    # Mean color of each material
    rgb_ref = np.array([[137, 131, 114],[104,90,74],[106,122,125],[117, 141, 153],[123,123,117]])
    
    cDist = np.zeros((5))
    for i in range(0,5): # Calculate distance to each material
        cDist[i] = np.sqrt(np.square(im_color[0] - rgb_ref[i,0]) +  np.square(im_color[1] - rgb_ref[i,1]) + np.square(im_color[2] - rgb_ref[i,2])   )
    

    # Find closest material
    minDist = np.min(cDist)
    minInd = np.argmin(cDist)
    mat = cName[minInd]
    
    return mat

# Perform edge detection and call material detection
def detectEdge():
    print("Detecting Edge")

    # Take image
    with picamera.PiCamera() as camera:
        output = np.empty((720, 1280, 3), dtype=np.uint8)
        camera.capture(output, 'rgb')
    print("Took Image")
    
    print("Computing Material")
    mat = closestMaterial(output[0:100,590:690,:])
    print(mat)
    
    imPic = np.mean(output, axis=2) # Convert to grayscale

    imBlur = gaussian_filter(imPic, sigma=3) # blur
    imThresh = np.copy(imBlur)
    imThresh[np.logical_and(imThresh > 50, imThresh < 130)] = 0 # Threshold
    
    
    imRaw = imBlur - imThresh
    
    vertSob = [[1,0,-1],[2,0,-2],[1,0,-1]]

    print("Thresholded Image")
    
    im = fftconvolve(imRaw, vertSob, mode='same') # FFT convolution with sobel filter
    
    print("Convolved Image")
    
    # Threshold edges
    n = 80
    im[im < n] = 0
    im[im > n] = n
    
    # Sum edges in each colomn
    eRow = im.sum(axis = 0) / 80
    eRow[0:5] = np.zeros((1,5))
    
    # Find peaks of edge histogram
    peaks, _ = find_peaks(eRow, distance = 250)
    
    sorted_peaks = np.argsort(eRow[peaks])
    if len(peaks) < 2:
        print("No edges found")
        return -1
    
    # Find the 2 largest peaks
    pk1 = peaks[sorted_peaks[-1]]
    pk2 = peaks[sorted_peaks[-2]]
    
    dist = abs(pk1 - pk2)
    print("Found Edges")
    print(dist)
    
    return dist

#while True:
#    detectEdge()
