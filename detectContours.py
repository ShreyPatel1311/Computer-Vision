import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-3.jpg')
resize = cv.resize(img, (960, 540), interpolation=cv.INTER_AREA)

blank = np.zeros(resize.shape, 'uint8')

#Edge Detection Algorithm
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(resize, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 50, 250)
cv.imshow('Canny', canny)

#Image Segmentation
ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', threshold)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} counter(s) are found')

conDrawn = cv.drawContours(blank, contours, -1, (0, 0, 255))
cv.imshow('Contours Drawn', conDrawn)

cv.waitKey(0)
cv.destroyAllWindows()
#Contours are like the boundary of the objects in the image. They are like curve which are formed by joining the joining the similar color boundaries.
#For more Info : https://pythongeeks.org/contour-detection-in-opencv/