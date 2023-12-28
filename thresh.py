import cv2 as cv

img = cv.imread("Photos/G-3.jpg")
resize = cv.resize(img, (960, 540))

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh) 

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold", thresh_inv)

#Adaptive Threshold
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding", adapt_thresh) 

cv.waitKey(0)
cv.destroyAllWindows()