import cv2
import numpy as np
import tensorflow as tf
from mtcnn import MTCNN
import time

p_time = 0

# Load the MTCNN model
model = MTCNN()

# Open the video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Detect faces and eyes in the frame
    faces = model.detect_faces(frame)

    # Draw bounding boxes around the faces and eyes
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        for key, value in face['keypoints'].items():
            cv2.circle(frame, value, 2, (0, 255, 0), 2)

    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time

    cv2.putText(frame, f'Fps: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 255, 100), 3)

    # Display the processed frame
    cv2.imshow("Frame", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the display window
cap.release()
cv2.destroyAllWindows()
