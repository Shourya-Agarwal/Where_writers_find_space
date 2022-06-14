# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:31:03 2022

@author: Agarw
"""

import cv2
#import numpy as np
n=cv2.imread("C:\\Users\\Agarw\\OneDrive\\Desktop\Litter-slogan.png")
#print(n)
out_guassian=cv2.GaussianBlur(n,(5,5),0)
cv2.imshow('normal', out_guassian)
cv2.imshow('guassian blur', out_guassian)
print(out_guassian)