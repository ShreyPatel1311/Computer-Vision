import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-4.jpg')

#Converting image to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)            #ksize, i.e, the tuple values must be an odd +integer.
cv.imshow('Blur', blur)

#Edge Cascade
cannyEdges = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', cannyEdges)

#Dilating the image
dilate = cv.dilate(cannyEdges, np.ones((7, 7), np.uint8),iterations=1) 
cv.imshow('Dilated', dilate)

cv.waitKey(0)
cv.destroyAllWindows()