import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

img = cv2.imread(os.path.join('mark2.png'))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
orb = cv2.ORB_create()    # OpenCV 3 backward incompatibility: Do not create a detector with `cv2.ORB()`.
key_pts, description = orb.detectAndCompute(img,None)
img_key_pts = cv2.drawKeypoints(img,key_pts,img,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.figure(figsize=(16,16))
plt.title('Interest Points')
plt.imshow(img_key_pts)
plt.show()
