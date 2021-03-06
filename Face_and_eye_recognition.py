import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()
while True:
    success, img = cap.read()

    results = faceDetection.process(img)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)
            # print(id, detection)
            # print(detection,score)
            #print(detection.location_data.relative_bounding_box)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime =cTime
    cv2.putText(img, f'Fps: {int(fps)}',(28,78),cv2.FONT_HERSHEY_PLAIN, 3 ,(0,255,0),2)
    cv2.imshow("image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

