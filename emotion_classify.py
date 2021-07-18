import test
import numpy as np
import cv2
import streamlit as st
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotions = ["Happy", "Sad", "Calm", "Energetic"]

def emotion_detect(frame):
    frame = cv2.resize(frame, (250, 250))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces  = detector.detectMultiScale(gray, scaleFactor=1.05,
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)
    if faces != ():
        for face in faces:
            x,y,w,h = face
            image = gray[y:y+h, x:x+w]
            image = cv2.resize(image, (48,48))
            image = image.reshape(48,48,1)
            emotion = emotions[test.predict_emotion(np.array([image]))]
            return emotion
    else:    
        return "Happy"






            
