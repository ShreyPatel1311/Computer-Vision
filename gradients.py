import cv2 as cv
import numpy as np

img = cv.imread("Photos/G-3.jpg")
resize = cv.resize(img, (960, 540))

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F) # type: ignore
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap) # type: ignore

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # type: ignore
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # type: ignore
combined_sobel = cv.bitwise_and(sobelx, sobely)
cv.imshow("Sobel", combined_sobel)

cv.waitKey(0)
cv.destroyAllWindows()