import cv2 as cv
import numpy as np

def translate(img, x, y):
    transMat = np.float32([
        [1,0,x],
        [0,1,y]
    ])  # type: ignore
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions) # type: ignore

def rotate(img, angle, rotPoint=None):
    if(rotPoint is None):
        rotPoint = (img.shape[1]//2, img.shape[0]//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, rotMat, dimensions)
   
img = cv.imread('Photos/G-1.png')
cv.imshow('Galaxy', img)

translated_img = translate(img, 50, 100)
cv.imshow('Translated Galaxy', translated_img)

rotate_img = rotate(img, 60)
cv.imshow('Rotated Galaxy', rotate_img)

cv.waitKey(0)
cv.destroyAllWindows()