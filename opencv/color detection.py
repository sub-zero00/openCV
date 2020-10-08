import cv2
import numpy as np


def empty(a):
    pass

img = cv2.imread("photo.png")
cv2.namedWindow("trackbars")

cv2.resizeWindow("trackbars",640,240)
cv2.createTrackbar("hue min","trackbars",44,179,empty)
cv2.createTrackbar("hue max","trackbars",179,179,empty)
cv2.createTrackbar("sat min","trackbars",37,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",122,255,empty)
cv2.createTrackbar("val max","trackbars",255,255,empty)
while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("hue min","trackbars")
    hmax = cv2.getTrackbarPos("hue max","trackbars")
    smin = cv2.getTrackbarPos("sat min","trackbars")
    smax = cv2.getTrackbarPos("sat max","trackbars")
    vmin = cv2.getTrackbarPos("val min","trackbars")
    vmax = cv2.getTrackbarPos("val max","trackbars")
    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])

    print(hmin,hmax,smin,smax,vmin,vmax)

    mask = cv2.inRange(imgHSV,lower,upper)
    imgR = cv2.bitwise_and(img,img,mask= mask)


    cv2.imshow("image",img)
    cv2.imshow("imageHSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("imgresult", imgR)

    cv2.waitKey(1)