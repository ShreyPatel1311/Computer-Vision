import cv2 as cv

img = cv.imread("Photos/lewis-hamilton.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f"Number of faces found are {len(face_rect)}")

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow("Face Detected", img)

cv.waitKey(0)
cv.destroyAllWindows()