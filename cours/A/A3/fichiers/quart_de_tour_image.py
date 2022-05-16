# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:59:56 2020

"""


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


"""
Rotation d'un quart de tour d'image de taille 2**p x 2**p
Diviser pour régner 
"""

def rotate(image):
    n = len(image)
    if n > 1:
        temp = np.copy(image[n//2:, :n//2])
        image[n//2:, :n//2] = rotate(image[n//2:, n//2:])
        image[n//2:, n//2:] = rotate(image[:n//2, n//2:])
        image[:n//2, n//2:] = rotate(image[:n//2, :n//2])
        image[:n//2, :n//2] = rotate(temp)
    return image

image = np.array(Image.open('R2D2.jpg'))
image = rotate(image)
plt.imshow(image)



"""
Version classique (itérative)
Rotation d'un quart de tour d'image de taille n x n
"""

def rotate(image):
    n = len(image)
    for i in range(n//2):
        for j in range(n//2):
			"à compléter"
    return image

image = np.array(Image.open('vador.jpg'))
image = rotate(image)
plt.imshow(image)



"""
Utilisation de ndimage.rotate
"""

from scipy import ndimage

image = np.array(Image.open('vador.jpg'))
image = ndimage.rotate(image, -90)
plt.imshow(image)




