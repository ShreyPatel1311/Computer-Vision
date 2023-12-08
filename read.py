import cv2 as cv

img = cv.imread('Photos/G-1.png')
cv.imshow('Galaxy', img)

cv.waitKey(0)