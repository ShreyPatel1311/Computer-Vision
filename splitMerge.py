import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-4.jpg')
resize = cv.resize(img, (960, 540))
blank = np.zeros(resize.shape[:2], 'uint8')
#cv.imshow('Image', resize)

b,g,r = cv.split(resize)

# cv.imshow('Blue', b)
# cv.imshow('Red', r)
# cv.imshow('Green', g)

blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])
cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)

Merged = cv.merge([b, g, r])
cv.imshow('Merged', Merged)

cv.waitKey(0)
cv.destroyAllWindows()