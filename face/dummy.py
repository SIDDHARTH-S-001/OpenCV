import cv2, time
cap = cv2.VideoCapture(0)
p_time = 0
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cascade_face = cv2.CascadeClassifier('/home/siddharth/catkin_ws/src/computer_vision/open_cv/face/haarcascade_frontalface_alt.xml')
# even simd haar and lp run at same fps as haar cascade 
cascade_eye = cv2.CascadeClassifier('/home/siddharth/catkin_ws/src/computer_vision/open_cv/face/haarcascade_eye.xml')

while True:
    success, frame = cap.read()
    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time
    faces = cascade_face.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors=15)
    for x, y, w, h in faces:
       frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    eyes = cascade_eye.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors=15)
    for x, y, w, h in eyes:
       frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, f'Fps: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 255, 100), 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
