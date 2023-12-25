import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), 'uint8')
rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), (255), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 0), -1)

#bitwise AND
bitAnd = cv.bitwise_and(rect, circle)
cv.imshow('AND',bitAnd)

#bitwise OR
bitOr = cv.bitwise_or(rect, circle)
cv.imshow('OR', bitOr)

#bitwise XOR
bitXor = cv.bitwise_xor(rect, circle)
cv.imshow('XOR', bitXor)

#bitwise NOT
bitNot = cv.bitwise_not(circle)
cv.imshow('NOT', bitNot)

cv.waitKey(0)
cv.destroyAllWindows()