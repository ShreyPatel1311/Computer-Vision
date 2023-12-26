import cv2 as cv
import numpy as np

img = cv.imread('Photos/G-1.png')
resize = cv.resize(img, (960, 540))
blank = np.zeros(resize.shape[:2], dtype='uint8')

circle = cv.circle(blank, (resize.shape[1]//2, resize.shape[0]//2), 200, (255, 0, 0), thickness=cv.FILLED)
#shape can be of any type , i.e, shape can be created through bitwise operations or directly built-in function.

mask = cv.bitwise_and(resize, resize, mask = circle)
cv.imshow('Masked Image', mask)

cv.waitKey(0)
cv.destroyAllWindows()