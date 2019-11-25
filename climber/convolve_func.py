# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:18:43 2019

@author: Andrew
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:15:52 2019

@author: Andrew
"""

import numpy as np

def convolve(imRaw, patchRaw):
    
    im = np.zeros((2048,2048)) # everything needs to be square pow of 2
    imShape = imRaw.shape
    im[0:imShape[0], 0:imShape[1]] = imRaw
    
    edge = np.zeros(im.shape)
    edge[0:3,0:3] = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    
    # Rotate to get conjugate
    patchRaw = np.rot90(patchRaw)  
    patchRaw = np.rot90(patchRaw)
    
    patchShape = patchRaw.shape
    
    patch = np.zeros(im.shape)
    patch[0:patchShape[0], 0:patchShape[1]] = patchRaw
    
    # Perform FFT
    im_F = np.fft.fft2(im)
    patch_F = np.fft.fft2(patch)
    edge_F = np.fft.fft2(edge)
    
    # Perform Convolution (First edge detect both, then conv together)
    imEdge_F = im_F * edge_F
    patchEdge_F = patch_F * edge_F
    conv_F = imEdge_F * patchEdge_F
    
    # IFFT and take abs val
    conv = np.absolute(np.fft.ifft2(conv_F))

    #Find Indices of Minimum
    convFindMin = conv[patchShape[0]:imShape[0]-patchShape[0], patchShape[1]:imShape[1]-patchShape[1]]
    indRaw = np.unravel_index(np.argmax(convFindMin, axis=None), convFindMin.shape)
    conv_coord = [indRaw[0]+patchShape[0], indRaw[1]+patchShape[1]]
    
    return conv_coord

def vert_edge(imRaw):
    
    im = np.zeros((2048,2048)) # everything needs to be square pow of 2
    imShape = imRaw.shape
    im[0:imShape[0], 0:imShape[1]] = imRaw
    
    sharp = np.zeros(im.shape)
    sharp[0:3,0:3] = [[0,-1,0],[-1,5,-1],[0,-1,0]]
    
    edge = np.zeros(im.shape)
    #edge[0:3,0:3] = [[1,0,-1],[2,0,-2],[1,0,-1]]
    edge[0:3,0:3] = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
    
    # Perform FFT
    im_F = np.fft.fft2(im)
    edge_F = np.fft.fft2(edge)
    sharp_F = np.fft.fft2(sharp)
    
    # Perform Convolution (First edge detect both, then conv together)
    imEdge_F = im_F * sharp_F * edge_F

    # IFFT and take abs val
    imEdgeRaw = np.absolute(np.fft.ifft2(imEdge_F))
    
    imEdge = imEdgeRaw[0:imShape[0], 0:imShape[1]]

    return imEdge

def basic_conv(imRaw, filtRaw):
    im = np.zeros((2048,2048)) # everything needs to be square pow of 2
    imShape = imRaw.shape
    im[0:imShape[0], 0:imShape[1]] = imRaw
    
    filt = np.zeros(im.shape)
    filt[0:3,0:3] = filtRaw
    
    #[[0,-1,0],[-1,5,-1],[0,-1,0]]
    
    #edge = np.zeros(im.shape)
    #edge[0:3,0:3] = [[1,0,-1],[2,0,-2],[1,0,-1]]
    #edge[0:3,0:3] = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
    
    # Perform FFT
    im_F = np.fft.fft2(im)
    filt_F = np.fft.fft2(filt)
    
    # Perform Convolution (First edge detect both, then conv together)
    imFilt_F = im_F * filt_F

    # IFFT and take abs val
    imFiltRaw = np.absolute(np.fft.ifft2(imFilt_F))
    
    imFilt = imFiltRaw[0:imShape[0], 0:imShape[1]]

    return imFilt
    