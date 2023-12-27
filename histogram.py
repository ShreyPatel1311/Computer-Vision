import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import rsa

img = cv.imread('Photos/G-2.jpg')
resize = cv.resize(img, (960, 540))
blank = np.zeros(resize.shape[:2], dtype='uint8')

# gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

# #Masking
# circle = cv.circle(blank, (resize.shape[1]//2, resize.shape[0]//2), 200, (255, 0, 0), thickness=cv.FILLED)
# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)

# # Gray Scale Histogram
# hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# #creating the histogram plot in matplotlib
# plt.figure()
# plt.title('Gray Scale Histogram')
# plt.xlabel('Bins')                                        #Bins refers to intensity of pixels.
# plt.ylabel('# of pixels')
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()

#Color Histogram
circle = cv.circle(blank, (resize.shape[1]//2, resize.shape[0]//2), 200, (255, 0, 0), thickness=cv.FILLED)
masked = cv.bitwise_and(resize, resize, mask=circle)
cv.imshow('Masked', masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')                                        #Bins refers to intensity of pixels.
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([resize], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()