import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/G-4.jpg')
resize = cv.resize(img, (960, 540))

#Gray Scale
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#HSV(High Saturation Value)
hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#LAB
lab = cv.cvtColor(resize, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(resize, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#Conversion of colors is required while using opencv and matplotlib, BGR 2 RGB conversion is used here.
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
#Conversion of HSV to GrayScale is not possible, HSV->BGR->GrayScale.