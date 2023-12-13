import cv2 as cv
import numpy as np

#height, width, color Channels
blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# #blue, green, red
# blank[200: 300, 300: 400] = 0, 0, 255
# cv.imshow('Red', blank)

# #draw a rectangle
# rect = cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=5)
# cv.imshow('Rectangle', rect)

# #draw a circle
# circle = cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (255, 0, 0), thickness=cv.FILLED)
# cv.imshow('Circle', circle)

# #draw a line
# line = cv.line(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 0, 255), thickness=5)
# cv.imshow('Line', line)

#add a text
text = cv.putText(blank, "Stay Hard!!!", (0, blank.shape[1]//2), cv.FONT_HERSHEY_COMPLEX, 2.0, (125, 0, 125), 5)
cv.imshow('Text', text)

cv.waitKey(0)