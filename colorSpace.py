import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("C:\\Users\\shrey\\Downloads\\abstract-minimalistic-text-typography-grayscale-focused-into-newspaper-3727390744.jpg")

#Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #HSV(High Saturation Value)
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# #LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# #BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)


# #Conversion of colors is required while using opencv and matplotlib, BGR 2 RGB conversion is used here.
# plt.imshow(rgb)
# plt.show()

cv.waitKey(1)
# success = cv.imwrite("gray_image_2.jpg", gray)
plt.imsave("grayscale_image.jpg", gray, cmap="gray")
cv.destroyAllWindows()
#Conversion of HSV to GrayScale is not possible, HSV->BGR->GrayScale.