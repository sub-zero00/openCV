import cv2

faceC = cv2.CascadeClassifier("haarcascades_frontalface_default.xml")
fwidth = 640
fheight = 480
cap = cv2.VideoCapture(0)
cap.set(3,fwidth)
cap.set(4,fheight)
cap.set(10,130)

while True:
    _, img = cap.read()
    faces = faceC.detectMultiScale(img, 1.1, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)
    cv2.imshow("photo", img)
    cv2.waitKey(1)