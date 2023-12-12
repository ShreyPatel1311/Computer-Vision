import cv2 as cv
import numpy as np

#height, width, color Channels
blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# #blue, green, red
# blank[200: 300, 300: 400] = 0, 0, 255
# cv.imshow('Red', blank)

rect = cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=5)
cv.imshow('Rectangle', rect)

cv.waitKey(0)