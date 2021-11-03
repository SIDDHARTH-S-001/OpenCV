import cv2
# for images
'''
img = cv2.imread("download.jfif") #remember that the image and the python progam must be in the same folder, here its 'scripts'
cv2.imshow("RoboVitics",img)
cv2.waitKey(0) # the image wil stay open for infinite amount of time
'''
# for video
'''
frameWidth = 640
frameHeight = 360
cap = cv2.VideoCapture('ezgif.com-gif-maker.mp4')

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'): #stating the q will stop the video, the video will automatically stop 
        break
'''
# webcam
frameWidth = 640
frameHeight = 360
cap = cv2.VideoCapture(0) # 0 is the code for the inbuilt camera (webcam)

# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

while True:
    success,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))

    cv2.imshow("Video",img) # changes the frame size/resolution to the user's convinence

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
