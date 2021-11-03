import cv2
import numpy as np
from Utilities import myUtilities as mu

def empty(a):
    pass
# cv2.namedWindow("params")
# cv2.createTrackbar("thresh1", "params",0,127,empty)
# cv2.createTrackbar("thresh2", "params",0,127,empty)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # if objCor == 3:
            #     objectType = "Tri"
            # elif objCor == 4:
            #     aspRatio = w / float(h)
            #     if aspRatio > 0.98 and aspRatio < 1.03:
            #         objectType = "Square"
            #     else:
            #         objectType = "Rectangle"
            # elif objCor > 4:
            #     objectType = "Circles"

            objectType = "Contour"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


#path = 'circ_sq.bmp'
#img = cv2.imread(path)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgContour = img.copy()
    imgLaplace = cv2.Laplacian(img, cv2.CV_64F)
    imgLaplace = np.uint8(imgLaplace)
    # imgGray = cv2.cvtColor(imgLaplace, cv2.COLOR_BGR2GRAY)
    # imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    #
    # t1 = cv2.getTrackbarPos("thresh1", "params")
    # t2 = cv2.getTrackbarPos("thresh2", "params")
    #
    imgCanny = cv2.Canny(imgLaplace, 50, 50)
    getContours(imgLaplace)

    imgBlank = np.zeros_like(img)
    imgStack = mu.stackImages(0.8, ([img, imgGray, imgBlur],
                                 [imgCanny, imgContour, imgBlank]))

    cv2.imshow("Stack", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break