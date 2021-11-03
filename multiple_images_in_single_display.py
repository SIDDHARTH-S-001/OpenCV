import cv2
import numpy as np
from Utilities import myUtilities
kernel = np.ones((5,5),np.uint8) # returns a numpy array filled with ones
print(kernel)
# path = "download.jfif"
# img = cv2.imread(path)
cap = cv2.VideoCapture(0) 
while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgErode = cv2.erode(imgDilation, kernel, iterations=2)
    StackedImages = myUtilities.stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgDilation, imgErode]))

    cv2.imshow("Video", StackedImages)  # changes the frame size/resolution to the user's convinence

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
