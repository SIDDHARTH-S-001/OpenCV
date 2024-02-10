import cv2

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')

# Load the cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier('path/to/haarcascade_eye.xml')

# Read the image
img = cv2.imread('path/to/image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Loop through the detected faces
for (x, y, w, h) in faces:
    # Draw a rectangle around the face
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Get the region of interest (ROI) for the eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Detect eyes in the ROI
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Loop through the detected eyes
    for (ex, ey, ew, eh) in eyes:
        # Draw a rectangle around the eye
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # Crop the eye region
        eye_gray = roi_gray[ey:ey+eh, ex:ex+ew]
        eye_color = roi_color[ey:ey+eh, ex:ex+ew]

        # Use the average brightness of the eye region to determine if the eye is open or closed
        brightness = cv2.mean(eye_gray)[0]
        if brightness > 100:
            print("Eye is open")
        else:
            print("Eye is closed")

# Display the image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
