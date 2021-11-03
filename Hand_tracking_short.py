import cv2
import mediapipe
from Hand_tracking import Hand_Detection as ht
import time

pTime = 0

cap = cv2.VideoCapture(0)

detector = ht.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=True)
    if(len(lmList)!=0):
        x0, y0 = lmList[0][1], lmList[0][2]
        x5, y5 = lmList[5][1], lmList[5][2]
        x6, y6 = lmList[6][1], lmList[6][2]
        cv2.line(img,(x0,y0),(x5,y5),(255,0,0),3)
        cv2.line(img,(x5,y5),(x6,y6),(0,255,0),3)

        # print(x0, y0,"0")
        # print(x5,y5,"5")
        # print(x6,y6,"6")
    cTime = time.time()
    fps = 1/(cTime-pTime)
    cv2.imshow("Hand", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break