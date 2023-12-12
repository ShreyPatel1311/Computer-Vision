import cv2 as cv

# works for both videos, images and liveVideos
def rescale(frame, scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    
    dimensions = (height, width)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# works only for Live Video
def changeRes(width, height):
    # capture properties : Each number represents a property for the capture.
    capture.set(3, width)                                                   # 3 references the width of capture
    capture.set(4, height)                                                  # 4 references the height of capture

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