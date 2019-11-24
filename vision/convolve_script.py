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
from convolve_func import convolve, vert_edge

plt.close('all')


imRaw = np.mean(imageio.imread('training/wood/img016.jpg'), axis=2)
patchRaw = np.mean(imageio.imread('training/wood_Template/patch018.jpg'), axis=2)

conv_coord = convolve(imRaw, patchRaw)

plt.figure()
plt.imshow(imRaw)

plt.figure()
plt.imshow(patchRaw)

plt.figure()
plt.imshow(imRaw[conv_coord[0]-100:conv_coord[0], conv_coord[1]-100:conv_coord[1]])

imEdge = vert_edge(imRaw)

plt.figure()
plt.imshow(imRaw)

plt.figure()
plt.imshow(imEdge)
