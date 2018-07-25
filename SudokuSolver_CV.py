# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 18:49:26 2018

@author: shabs
"""

import cv2
import numpy as np
import csv
import os
import pytesseract as pt
from PIL import Image

os.remove('/home/shabs/Documents/Python Progs openCV/test.csv')
img = cv2.imread('/home/shabs/Documents/Python Progs openCV/SampleImages/sudoku.png')
#print(np.shape(img))
img = cv2.resize(img,(431,431))
#cv2.imshow('Input',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_ ,gr = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#print(gray)
#cv2.imshow('Gray',gr)
i = 0
j = 0
k = 0

edges = cv2.Canny(gray,20,50,apertureSize=3)
im, cnt, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,cnt,-1,(0,255,0),1)
for c in cnt:
    ar = cv2.contourArea(c)
    newImg = img.copy()
    #print(ar)
    (x,y,w,h) = cv2.boundingRect(c)
    #cv2.drawContours(img,c,-1,(0,255,0),1)
    if(h>18 and h<46 and w>10 and w<47 and (abs(x-j)>7 or abs(y-k)>7)):
        #print("h = " + str(h) + "   w = "+str(w))
        #print(gr.item(x,y))
        #print("j = " + str(j) + "   k = "+str(k))
        #print("Contour Area = "+str(ar))
        #print(np.size(c))
        #print(c)
        h,w = 28,28
        a=[]
        x1 = x
        x2 = x+w
        y1 = y
        y2 = y+h
        #print(x1)
        #print(x2)
        cv2.rectangle(newImg,(x1,y1),(x2,y2),(0,255,0),2)
        roi = gr[y1:y2,x1:x2]
        cv2.imwrite('/home/shabs/Documents/Python Progs openCV/SampleImages/roi.png',roi)
        #cv2.imwrite('image.jpg',image)
        word = (pt.image_to_string(Image.open('/home/shabs/Documents/Python Progs openCV/SampleImages/roi.png'), lang='eng'))
    
        #print(roi)
        #cv2.imshow('ROI',roi)
        #cv2.imshow('Image',newImg)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        for l in range(0,28):
            for b in range(0,28):
                #print(gr.item(x+l,y+b))
                a.append(1 if(roi[b][l]==255) else 0)
        myFile = open('test.csv','a', newline = '')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows([a]) 
        print("Wiritng to file done")
        #cv2.imshow('Contour',newImg)
        #cv2.waitKey(0)
        j = x
        k = y
        i = i+1
    #cv2.waitKey(500)
#cv2.imshow('Edges',img)
cv2.imshow('Contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#import SudokuSolver2