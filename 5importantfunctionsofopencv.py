import cv2
path = "download.jfif"
img = cv2.imread(path,0)
'''
# we can convert images to Gray scale in 2 ways, one is shown below
# img = cv2.imread(path)
# imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img)
cv2.imshow("image in GRAY", imgGray)
cv2.waitKey()


# and the other is
img = cv2.imread(path,0) # this will real the image in Gray scale itself
cv2.imshow("img",img)
cv2.waitKey()

# blurring the image
img = cv2.imread(path,0)
imgBlur = cv2.GaussianBlur(img,(15,15),0)
cv2.imshow("Blurred image", imgBlur)
cv2.waitKey(0)

# image canny(detecting edges)
imgCanny =  cv2.Canny(img,100,100) #we can inscrese or decrease the threshold to get better outputs
cv2.imshow('image canny',imgCanny)
cv2.waitKey(0)
'''
# image dialation and erosion

