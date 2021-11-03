import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

cone = cv2.imread('dataset/Valid/cone/aug_0_1080.png')
cone_gray = cv2.cvtColor(cone, cv2.COLOR_BGR2GRAY)
print(cone_gray.dtype)
contours, heirarchy = cv2.findContours(cone_gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contour_array = np.zeros(cone.shape)

for i in range(len(contours)):
  if heirarchy[0][i][3] == -1:
    cv2.drawContours(contour_array, contours, -1,(255,0,0),3)

cv2.imshow('image', contour_array)
cv2.waitKey(5000)


