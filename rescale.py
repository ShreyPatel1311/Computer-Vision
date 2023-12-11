import cv2 as cv

def rescale(frame, scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    
    dimensions = (height, width)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('Videos/Nebula.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized);
    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()