import cv2
import mediapipe as mp
import itertools
import time

p_time = 0
mp_face_mesh = mp.solutions.face_mesh
face_meshes = mp_face_mesh.FaceMesh(max_num_faces = 1)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    face_mesh_results = face_meshes.process(frame[:, :, ::-1])

    left_eye_indices = list(set(itertools.chain(mp_face_mesh.FACEMESH.LEFT_EYE)))
    right_eye_indices = list(set(itertools.chain(mp_face_mesh.FACEMESH.RIGHT_EYE)))
    
    if face_mesh_results.multi_face_lankmarks:
        for face_no, face_landmarks in enumerate(face_mesh_results.multi_face_landmarks):
            for left_eye_index in left_eye_indices[:2]:
                print(face_landmarks.landmark[left_eye_index])
            for right_eye_index in right_eye_indices[:2]:
                print(face_landmarks.landmark[right_eye_index])

    if face_mesh_results.multi_face_landmarks:

        for face_landmarks in face_mesh_results.multi_face_landmarks:

            mp_drawing.draw_landmarks(image=frame, 
                                    landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,
                                    landmark_drawing_spec=None, 
                                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
            
            mp_drawing.draw_landmarks(image=frame, landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,
                                    landmark_drawing_spec=None, 
                                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

