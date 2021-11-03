import cv2
import numpy as np
# creating a blank image (staring with just 1 channel either black or white

img = np.zeros((512,512)) # note that the zeros method in numpy needs 2 pairs of brackets
cv2.imshow("Blank image",img)

img3c = np.zeros((512,512,3))  # ----->  (1)

print(img3c.shape)

# print(img3c)  # here we can see that the image is now presented as a matriz with zeroes followed by '.', which means that the elements of this matrix are floating pint values
# but we need the elements to be integers, so we do this instead of (1)
img3cnew = np.zeros((512,512,3),np.uint8)
print(img3cnew)

# now, to make the blank image blue
# img3cnew[:] = 255,0,0 #makes the image appear in blue as open cv follows BGR convention
#img3cnew[:] = 0,255,0 # makes the image appears green
#img3cnew[:] = 0,0,255 # makes the image appear in red
#img3cnew[:] = 255,255,0 # image appears cyan

#img3cnew[:] = 255,0,255 # image appears pink
#img3cnew[:] = 0,255,255 # image appears yellow
#img3cnew[:] = 255,255,255 # image appears white

# now just coloring a part of the image
#img3cnew[100:300] = 255,0,0 # this just colors a part of the image with blue while the others appear black as always

# now to draw a line
cv2.line(img3cnew,(0,0),(100,100),(255,0,0),5) # draws a blue color line from (0,0) to (100,100) of thichness 5
cv2.rectangle(img3cnew,(500,500),(300,300),(255,255,0),10) # draws arectangle between the 2 specified points in the given color and thinkness
cv2.rectangle(img3cnew,(500,0),(300,200),(255,0,255),cv2.FILLED) # can be used to fill the rectangle using cv2.FILLED instead of giving it a thickness
cv2.circle(img3cnew,(150,400),25,(255,255,255),3) # circle with given center, radius and thickness
cv2.circle(img3cnew,(256,256),45,(0,255,255),cv2.FILLED) # circle with given center, radius and filling color
cv2.putText(img3cnew,"Draw Shape", (200,200),cv2.FONT_ITALIC,1,(0,255,0),2) # for the text
cv2.imshow("3 channel blank image", img3cnew) # still comes out to be black and completely blank
cv2.waitKey(0)


