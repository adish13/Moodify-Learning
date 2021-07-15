from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
import pandas as pd
import numpy as np
from pickle import load
from sklearn.preprocessing import MinMaxScaler

model = Sequential([  
  InputLayer(input_shape=7),
  Dense(5, activation = 'relu'),
  Dense(4, activation = 'softmax')
  ])
model.load_weights("music_weights.hdf5")
model.compile(optimizer="Adam",loss='sparse_categorical_crossentropy',metrics='accuracy')

scaler = load(open('scaler.pkl', 'rb'))
emotions = ["Calm", "Energetic", "Happy", "Sad"]

def recommend_music(hist, mood):
    x = hist[["danceability", "acousticness", "energy", "instrumentalness", "valence", "loudness", "speechiness"]]
    x = scaler.transform(x)
    predictions = model.predict(x)
    index_moods = np.argmax(predictions, axis =1)
    moods = []
    for index in index_moods:
        moods.append(emotions[index])
    hist["moods"] = moods
    return hist[hist["moods"] == mood]

