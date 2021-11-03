# this part covers wherein we will set poins for the matrix (for warp perspective) by clicking on specific points in the image

# NEEDS IMPROVEMENT !!!

import cv2
import numpy as np

circles = np.zeros((4,2),np.uint8)
counter = 0
print(circles)

def mousepts(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(circles
)


img = cv2.imread("cards.jpeg")

while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])  # in this part we use ms paint, where we moved the mouse to gte the pixels of the king card so that we coiuld isolate it
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Bird's view of king alone", imgOutput)

    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mousepts, None)
    cv2.waitKey(0)

