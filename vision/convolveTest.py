# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:20:40 2019

@author: Andrew
"""

from scipy import signal
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

#sig = np.random.randn(1000)
#autocorr = signal.fftconvolve(sig, sig[::-1], mode='full')
#
#fig, (ax_orig, ax_mag) = plt.subplots(2, 1)
#ax_orig.plot(sig)
#ax_orig.set_title('White noise')
#ax_mag.plot(np.arange(-len(sig)+1,len(sig)), autocorr)
#ax_mag.set_title('Autocorrelation')
#fig.tight_layout()
#fig.show()
#
#face = misc.face()
#misc.imsave('face.png', face) # First we need to create the PNG file
#
#face = misc.imread('face.png')


face = misc.face(gray=True)

face = misc.imread('pics/zebra1.jfif',flatten=True)
#kernel = np.outer(signal.gaussian(70, 8), signal.gaussian(70, 8))
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

blurred = signal.fftconvolve(face, kernel, mode='same')

patch = face[300:400, 450:550]
plt.imshow(patch)
plt.figure()
patchBlur = signal.fftconvolve(patch, kernel, mode='same')

plt.imshow(patchBlur)

fig, (ax_orig, ax_kernel, ax_blurred) = plt.subplots(3, 1,figsize=(6, 15))
ax_orig.imshow(face, cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_kernel.imshow(kernel, cmap='gray')
ax_kernel.set_title('Gaussian kernel')
ax_kernel.set_axis_off()
ax_blurred.imshow(blurred)
ax_blurred.set_title('Blurred')
ax_blurred.set_axis_off()

plt.figure()
tempMatch = signal.fftconvolve(face, patch, mode='same')
plt.imshow(tempMatch)

fig.show()
