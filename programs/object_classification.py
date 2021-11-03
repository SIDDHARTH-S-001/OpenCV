import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from keras.models import load_model
import numpy as np
import time
from keras.preprocessing import image

pTime = 0

lbl = ['cone', 'ball']

model = load_model('1.h5')
img = cv2.imread('cone.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = image.img_to_array(img)
#img = np.expand_dims(img, axis=0)

#cap = cv2.VideoCapture('video.mp4')

pTime = 0
#cv2.imshow('img', img)
result = model.predict(img)
cv2.waitKey(100)
# while True:
#     ret, img = cap.read()
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     result = model.predict(img)
#     # train_batch.class_indices
#
#     if result[0][0] == 1:
#         prediction = 'ball'
#     else:
#         prediction = 'cone'
#
#     print(prediction)
#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime
#     cv2.putText(img, f'Fps: {int(fps)}', (28, 78), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
#     #print(img.shape)
#     cv2.imshow('image', img)
#     cv2.waitKey(10)
#
