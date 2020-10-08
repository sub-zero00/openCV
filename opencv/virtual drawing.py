import cv2
import numpy as np
fwidth = 640
fheight = 480
cap = cv2.VideoCapture(1)
cap.set(3,fwidth)
cap.set(4,fheight)
cap.set(10,130)

myColors = [[27,84,80,46,255,186]]
points = []

def getcontours(img):
    contours,hier = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgR, cnt, -1, (255, 255, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

    return x+w//2,y

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0][:3])
    upper = np.array(myColors[0][3:])
    newP = []
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("mask",mask)
    x, y = getcontours(mask)
    cv2.circle(imgR,(x,y),10,(255,255,0),cv2.FILLED)
    if x != 0 and y != 0:
        newP.append([x, y])
    return newP

def draw(points):
    for point in points:
        cv2.circle(imgR,(point[0],point[1]),10,(255,255,0),cv2.FILLED)


while True:
    success, img = cap.read()
    imgR = img.copy()
    newP = findColor(img, myColors)
    if len(newP) != 0:
        for n in newP:
            points.append(n)
    if len(points) != 0:
        draw(points)
    cv2.imshow("result", imgR)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break