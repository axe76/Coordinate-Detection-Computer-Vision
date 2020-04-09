# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:03:12 2020

@author: ACER
"""

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\ACER\Desktop\AI\slam.png")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

'''cv2.line(img,(900,456),(900,556),3)
for i in range(0,3):
    print(img[900,456,i])'''

lower_blue = np.array([110,86,0]) 
upper_blue = np.array([150,255,255])
blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)

lower_yellow = np.array([200,0,60])
upper_yellow = np.array([250,5,100])
yellow_mask = cv2.inRange(hsv,lower_yellow,upper_yellow)

lower_red = np.array([150,86,0])
upper_red = np.array([250,255,255])
red_mask = cv2.inRange(hsv,lower_red,upper_red)

_,contours_b,_ = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#_,contours_y,_ = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
_,contours_r,_ = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours_b:
    area = cv2.contourArea(contour)
    if area>1000:
        cv2.drawContours(img,contour,-1,(0,255,0),3)
        bounding_box = cv2.boundingRect(contour)
        cv2.line(img,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),3)
        print("Blue Coord = ",bounding_box[0]+bounding_box[2]/2,bounding_box[1]+bounding_box[3]/2)
        
for contour in contours_r:
    area = cv2.contourArea(contour)
    if area>1000:
        cv2.drawContours(img,contour,-1,(0,255,0),3)
        bounding_box = cv2.boundingRect(contour)
        cv2.line(img,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),3)
        print("Red Coord = ",bounding_box[0]+bounding_box[2]/2,bounding_box[1]+bounding_box[3]/2)

cv2.imshow('image',img)
#cv2.imshow('blue_mask',blue_mask)
#cv2.imshow('yellow_mask',yellow_mask)
#cv2.imshow('red_mask',red_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()