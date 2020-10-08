import cv2
import numpy as np

def getcontours(img):
    contours,hier = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            objcol = len(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),3)
            if objcol == 3 :
                objectType = "ucgen"
            elif objcol == 4 :
                objectType = "dikdortgen"
            else :
                objectType = "daire"
            cv2.putText(imgContour,objectType,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)


img = cv2.imread("adsiz.png")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgb = cv2.GaussianBlur(img1,(7,7),1)
imgc = cv2.Canny(imgb,50,50)
imgContour = img.copy()
getcontours(imgc)
cv2.imshow("photo",imgContour)

cv2.waitKey(0)