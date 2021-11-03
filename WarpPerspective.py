import cv2
import numpy as np

img = cv2.imread("cards.jpeg")

width, height = 250,350
pts1 = np.float32([[241,262],[434,223],[285,550],[500,500]]) # in this part we use ms paint, where we moved the mouse to gte the pixels of the king card so that we coiuld isolate it
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Original image",img)
cv2.imshow("Bird's view of king alone",imgOutput)
cv2.waitKey(0)