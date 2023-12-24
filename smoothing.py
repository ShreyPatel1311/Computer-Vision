import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-1.png')
resize = cv.resize(img, (960, 540))
cv.imshow('G-1', resize)

#Averaging(Blur the most among all naturally)
avg = cv.blur(resize, (9, 9))
cv.imshow('Averaging', avg)

#Gaussian Blur(Natural Blur than avergaing)
gauss = cv.GaussianBlur(resize, (9, 9), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur(get a smudge type image looks like a painting)
median = cv.medianBlur(resize, 9)
cv.imshow('Median', median)

#Bilateral Blur(applies Blur but retains edges)
bilat = cv.bilateralFilter(resize, 10, 30, 30)
cv.imshow('Bilateral', bilat)

cv.waitKey(0)
cv.destroyAllWindows()