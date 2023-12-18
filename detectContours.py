import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-3.jpg')
resize = cv.resize(img, (960, 540), interpolation=cv.INTER_AREA)

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(resize, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 50, 250)
cv.imshow('Canny', canny)


#contours are the list of all the coord of contour(shapes like circle, rect, square, etc) present in the image.
#heirarchy is the defined structure which contains the info related to the contour structures like rect inside a circle, etc
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} counter(s) are found')

cv.waitKey(0)
cv.destroyAllWindows()