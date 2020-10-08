import cv2
import numpy as np

faceC = cv2.CascadeClassifier("haarcascades_frontalface_default.xml")
img = cv2.imread("resim.jpg")


#imgG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceC.detectMultiScale(img,1.1,10)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)


cv2.imshow("photo",img)
cv2.waitKey(0)