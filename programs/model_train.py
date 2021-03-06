import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import matplotlib as plt
import numpy as np
from keras.utils.np_utils import to_categorical
import random, shutil
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dropout, Conv2D, Flatten, Dense, MaxPooling2D, BatchNormalization
from keras.models import load_model
from pyflowchart import *

st = StartNode('a_pyflow_test')
op = OperationNode('do something')
cond = ConditionNode('Yes or No?')
io = InputOutputNode(InputOutputNode.OUTPUT, 'something...')
sub = SubroutineNode('A Subroutine')
e = EndNode('a_pyflow_test')


def generator(dir, gen=image.ImageDataGenerator(rescale=1. / 255), shuffle=True, batch_size=1, target_size=(255, 255),
              class_mode='categorical'):
    return gen.flow_from_directory(dir, batch_size=batch_size, shuffle=shuffle, color_mode='rgb',
                                   class_mode=class_mode, target_size=target_size)


BS = 32
TS = (255, 255)
train_batch = generator('dataset/train', shuffle=True, batch_size=BS, target_size=TS)
valid_batch = generator('dataset/Valid', shuffle=True, batch_size=BS, target_size=TS)
SPE = len(train_batch.classes) // BS
VS = len(valid_batch.classes) // BS
print(SPE, VS)

model = Sequential([
    Conv2D(16, kernel_size=(3, 3), activation='relu', input_shape=(255, 255, 3)),
    MaxPooling2D(pool_size=(1, 1)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(1, 1)),
    # 32 convolution filters used each of size 3x3
    # again
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(1, 1)),

    # 64 convolution filters used each of size 3x3
    # choose the best features via pooling

    # randomly turn neurons on and off to improve convergence
    Dropout(0.25),
    # flatten since too many dimensions, we only want a classification output
    Flatten(),
    # fully connected to get all relevant data
    Dense(64, activation='relu'),
    # one more dropout for convergence' sake :)
    Dropout(0.5),
    # output a softmax to squash the matrix into output probabilities
    Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(generator=train_batch, validation_data=valid_batch, epochs=15, steps_per_epoch=SPE, validation_steps=VS)

model.save('model_rgb.h5', overwrite=True)

# define the direction the connection will leave the node from
sub.set_connect_direction("right")

st.connect(op)
op.connect(cond)
cond.connect_yes(io)
cond.connect_no(sub)
sub.connect(op)
io.connect(e)

fc = Flowchart(st)
print(fc.flowchart())
