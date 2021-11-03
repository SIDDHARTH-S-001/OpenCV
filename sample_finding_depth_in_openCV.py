import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("params")
cv2.createTrackbar("thresh1", "params",0,127,empty)
cv2.createTrackbar("thresh2", "params",0,127,empty)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgLaplace = cv2.Laplacian(img, cv2.CV_64F)
    imgLaplace = np.uint8(imgLaplace)
    imgGray = cv2.cvtColor(imgLaplace,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    t1 = cv2.getTrackbarPos("thresh1", "params")
    t2 = cv2.getTrackbarPos("thresh2", "params")

    imgCanny = cv2.Canny(imgLaplace,t1,t2)

    cv2.imshow("imgCan", imgGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

