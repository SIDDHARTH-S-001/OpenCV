import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import time
#import serial

#ser = serial.Serial('com3', 9600)

pTime = 0
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
#val = (143.0/640)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Flip on horizontal
        image = cv2.flip(image, 1)
        # Set flag
        image.flags.writeable = False
        # Detections
        results = hands.process(image)
        # Set flag to true
        image.flags.writeable = True
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Detections
        image_height = image.shape[0]
        image_width = image.shape[1]

        i_m = []
        i_p = []
        i_d = []
        i_t = []

        m_m = []
        m_p = []
        m_d = []
        m_t = []

        r_m = []
        r_p = []
        r_d = []
        r_t = []

        p_m = []
        p_p = []
        p_d = []
        p_t = []



        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )

                i_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width)
                i_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height)
                i_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z)

                i_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width)
                i_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height)
                i_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z)

                i_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width)
                i_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height)
                i_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z)

                i_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                i_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
                i_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z)



                m_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width)
                m_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height)
                m_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z)

                m_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width)
                m_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height)
                m_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z)

                m_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width)
                m_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height)
                m_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z)

                m_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width)
                m_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height)
                m_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z)



                r_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width)
                r_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height)
                r_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z)

                r_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width)
                r_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height)
                r_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z)

                r_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width)
                r_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height)
                r_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z)

                r_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width)
                r_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height)
                r_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z)


                p_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width)
                p_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height)
                p_m.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_MCP].z)

                p_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width)
                p_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height)
                p_p.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_PIP].z)

                p_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width)
                p_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height)
                p_d.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_DIP].z)

                p_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width)
                p_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height)
                p_t.append(results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_TIP].z)

                #ser.write(i_m)


                print(p_p)

        # Save our image
        #cv2.imwrite(os.path.join('Output Images', '{}.jpg'.format(uuid.uuid1())), image)

        #print(image.shape) # shape = (480,640,3) : height, width, channels (3 for rgb)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, f'Fps: {int(fps)}', (28, 78), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        cv2.imshow('Hand Tracking', image)


        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()