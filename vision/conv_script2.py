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
import matplotlib.pyplot as plt
import imageio
from convolve_func import convolve, vert_edge, basic_conv
import scipy.signal as sig
from scipy.ndimage.filters import gaussian_filter

plt.close('all')


imRaw = np.mean(imageio.imread('training3/img142.jpg'), axis=2)

imOrg = np.copy(imRaw)

imBlur = gaussian_filter(imRaw, sigma=4)

imOrg = np.copy(imBlur)

imThresh = np.copy(imBlur)

imThresh[np.logical_and(imThresh > 40, imThresh < 140)] = 0

#imRaw[imRaw > 200] = 200
#imRaw[imRaw < 100] = 100

imRaw = imBlur - imThresh

vertSob = [[1,0,-1],[2,0,-2],[1,0,-1]]
vertEdge = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
totEdge = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
blur = [[1/16, 1/8, 1/16],[1/8, 1/4, 1/8],[1/16, 1/16,1/8]]

sharp = [[0,-1,0],[-1,5,-1],[0,-1,0]]


im = basic_conv(imRaw, vertSob)
n = 80
im[im < n] = 0
im[im > n] = n

eRow = im.sum(axis = 0) / 80
eRow[0:5] = np.zeros((1,5))

peaks, _ = sig.find_peaks(eRow, distance = 250)


#print(peaks)

sorted_peaks = np.argsort(eRow[peaks])
pk1 = peaks[sorted_peaks[-1]]
pk2 = peaks[sorted_peaks[-2]]

dist = abs(pk1 - pk2)
print(dist)

plt.figure()
plt.imshow(imOrg)

plt.figure()
plt.imshow(imThresh)

plt.figure()
plt.imshow(imRaw)

plt.figure()
plt.imshow(imBlur)

plt.figure()
plt.imshow(im)
plt.vlines([pk1, pk2], 0, 720, colors = 'r')

plt.figure()
plt.plot(range(0,1280), eRow)
#plt.plot(peaks, eRow[peaks],'ro')
plt.plot(pk1, eRow[pk1],'ro', pk2,eRow[pk2], 'ro')

plt.show()