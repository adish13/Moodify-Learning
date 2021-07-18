import tensorflow.keras
import tensorflow
import math
import numpy as np
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization

data_augmentation = tensorflow.keras.Sequential(
  [
    tensorflow.keras.layers.experimental.preprocessing.RandomFlip("horizontal", 
                                                 input_shape=(48,48,1)),
    tensorflow.keras.layers.experimental.preprocessing.RandomRotation(0.1),
    tensorflow.keras.layers.experimental.preprocessing.RandomZoom(0.05),
  ]
)

model = Sequential([  
        tensorflow.keras.layers.InputLayer(input_shape=(48, 48, 1)),
        data_augmentation,
        Conv2D(16, kernel_size=(3, 3), activation='relu', padding ='same'),
        Conv2D(16, kernel_size=(3, 3), activation='relu', padding = 'same'),
        BatchNormalization(),
        MaxPool2D(pool_size=(2, 2)),
        Conv2D(32, kernel_size=(3, 3), activation='relu', padding ='same'),
        Conv2D(32, kernel_size=(3, 3), activation='relu', padding ='same'),
        BatchNormalization(),
        MaxPool2D(pool_size=(2, 2)),
        Dropout(0.25),
        Conv2D(64, kernel_size=(3, 3), activation='relu', padding ='same'),
        Conv2D(64, kernel_size=(3, 3), activation='relu', padding ='same'),
        BatchNormalization(),
        MaxPool2D(pool_size=(2, 2)),
        Dropout(0.25),
        Conv2D(128, kernel_size=(3, 3), activation='relu', padding ='same'),
        Conv2D(128, kernel_size=(3, 3), activation='relu', padding ='same'),
        BatchNormalization(),
        MaxPool2D(pool_size=(2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.25),
        Dense(64, activation = "relu"),
        Dropout(0.25),
        Dense(32,activation='relu'),
        Dropout(0.25),
        Dense(5,activation='softmax')
        ])

model.load_weights("weights.hdf5")
model.compile(optimizer="Adam",loss='sparse_categorical_crossentropy',metrics='accuracy')

def predict_emotion(image):
  prediction = model.predict(image)[0]
  emotion = [0,0,0,0]
  emotion[0] = prediction[1]
  emotion[1] = prediction[2]
  emotion[2] = prediction[4] + 0.5*prediction[1] + 0.25*prediction[2]
  emotion[3] = 1.2*prediction[3] + 0.3*prediction[1] + 0.3*prediction[0]
  emotion = np.argmax(emotion)
  return emotion

