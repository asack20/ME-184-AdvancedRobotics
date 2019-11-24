# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:20:40 2019

@author: Andrew
"""
from IPython import get_ipython
def __reset__(): get_ipython().magic('reset -sf')

from scipy import signal
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import imageio

plt.close('all')


imRaw = np.mean(imageio.imread('pics/zebra1.jfif'), axis=2)
im = np.zeros((1024,1024))
im[0:705, 0:1000] = imRaw
#patch = misc.imread('pics/zebra1.jfif',flatten=True)

edge = np.zeros((1024,1024))
edge[0:3,0:3] = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

patch = im[300:400, 450:550]

plt.figure()
plt.imshow(patch)

patch = np.rot90(patch)

#plt.figure()
#plt.imshow(patch)

patch = np.rot90(patch)

#plt.figure()
#plt.imshow(patch)


target = np.zeros(im.shape)
target[0:100, 0:100] = patch

#plt.figure()
#plt.imshow(target)

im_F = np.fft.fft2(im)
target_F = np.fft.fft2(target)
edge_F = np.fft.fft2(edge)

plt.figure()
plt.imshow(im)

#plt.figure()
#plt.imshow(target)



conv_F = im_F * target_F
imEdge_F = im_F * edge_F
targetEdge_F = target_F * edge_F

convEdge_F = imEdge_F * targetEdge_F


conv = np.fft.ifft2(conv_F)
imEdge = np.fft.ifft2(imEdge_F)
convEdge = np.absolute(np.fft.ifft2(convEdge_F))

#imEdge = imEdge.real
convFindMin = convEdge[110:990,110:690]
indRaw = np.unravel_index(np.argmax(convFindMin, axis=None), convFindMin.shape)
indAdj = [indRaw[0]+110, indRaw[1]+110]
#plt.figure()
#plt.imshow(np.absolute(conv))

plt.figure()
plt.imshow(convEdge)

plt.figure()
plt.imshow(im[indAdj[0]-100:indAdj[0], indAdj[1]-100:indAdj[1]])

imEdge = np.absolute(imEdge)

plt.figure()
plt.imshow(imEdge)

#thresh = 120
#super_threshold_indices = imEdge < thresh
#imEdge[super_threshold_indices] = 0
#
#plt.figure()
#plt.imshow(imEdge)

