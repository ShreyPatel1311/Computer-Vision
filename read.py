import cv2 as cv

# img = cv.imread('Photos/G-1.png')
# cv.imshow('Galaxy', img)
#cv.waitKey(0)

#Reading videos
capture = cv.VideoCapture('Videos/623064168.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
