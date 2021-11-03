import cv2
path = "download.jfif"
img = cv2.imread(path)
print(img.shape)
cv2.imshow("Robovitics",img)

# resizing the image (remember,increasing the size wont increase the quality, but increases the number of pixels
width, height = 100, 100
imgResized = cv2.resize(img,(width,height))
cv2.imshow("Image Resized", imgResized)
print(imgResized.shape)    # shape method gets us the dimesnsions of the image and the number of channels, 3 implies for R,G and B

imgCropped =  img[0:150,0:225] # the 1st parameter is the range of height/y-value, and the 2nd parameter is the range of width/x-value.
# the +ve x axis in cartesian coordinates is the +ve x axis in open cv as well
# however the -ve y axis in cartesian coordinates is the +ve y axis in open cv
cv2.imshow("img cropped on y", imgCropped)

#now resizing the cropped image to the dimensions of the original image
imgCroppedResized = cv2.resize(imgCropped,(img.shape[1],img.shape[0])) #here the 2nd argument asks for the dimensions, wherei we give the 1st one to be width and 2nd one to be height
cv2.imshow("cropped image resized ot original size",imgCroppedResized)
cv2.waitKey(0)


