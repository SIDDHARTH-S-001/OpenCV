import cv2
import numpy as np

def mousepts(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv2.imread("cards.jpeg")
cv2.imshow("Original Image",img)
cv2.setMouseCallback("Original Image",mousepts,None)
cv2.waitKey(0)