import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from scipy import misc, ndimage

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def plots(img_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(img_arr, axes):
        ax.imshow(img)
        ax.axis('off')
        plt.tight_layout()
        plt.show()

gen = ImageDataGenerator(rotation_range=30, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, channel_shift_range=10, horizontal_flip=True)



img_path = 'valid_dataset/black cone.jpeg'

# assert os.path.isfile(img_path)

img = np.expand_dims(ndimage.imread(img_path), 0)
plt.show(img[0])

aug_iter = gen.flow(img)

aug_img = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]

plots(aug_img, figsize=(20,7), rows =2)



