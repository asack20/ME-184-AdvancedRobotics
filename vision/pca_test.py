# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:54:45 2019

@author: Andrew
"""

#import sklearn
import imageio
import numpy as np
from time import time
import logging

import matplotlib.pyplot as plt
import cv2

plt.close('all')

sz = (100,100,3)

X = np.zeros((30, 100*100*3))

for i in range(1, 31):
    
    im = imageio.imread('training/brick_Template/patch%03d.jpg'%i)
    vec = im.flatten()
    X[i-1,:] = vec

# Compute the eigenvectors from the stack of images created
print("Calculating PCA ", end="...")
maxComp = 5
mean, eigenVectors = cv2.PCACompute(X, mean=None, maxComponents=maxComp)
print ("DONE")

avgIm = mean.reshape(sz)

eigenIms = []; 

print("Reshaping Eigen Images ", end="...")
for eigenVector in eigenVectors:
    eigenIm = eigenVector.reshape(sz)
    eigenIms.append(eigenIm)
print ("DONE")

 # Create window for displaying Mean Face
plt.figure()
plt.imshow(avgIm.astype(int))
plt.title('Average Image')
 
for i in range(0, maxComp):
    plt.figure()
    plt.imshow((eigenIm[i]+avgIm).astype(int))
    plt.title('Eigen Image #%d'%(i+1))


avg_color = np.mean(avgIm, axis = (0,1))
print('brick')
print(avg_color)
#pca = PCA(n_components=29)
#pca.fit(X)  
#
#
#print(pca.explained_variance_ratio_)  
#
#print(pca.singular_values_)  
#
#pca.components_.reshape((29, 100, 100))

# #############################################################################
