import test
import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
emotions = ["Happy", "Sad", "Calm", "Energetic"]

def emotion_detect(frame):
    frame = cv2.resize(frame, (250, 250))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces  = detector.detect_faces(frame)

    if faces != []:
        for face in faces:
            x,y,w,h = face["box"]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            image = gray[y:y+h, x:x+w]
            image = cv2.resize(image, (48,48))
            image = image.reshape(48,48,1)
            emotion = emotions[test.predict_emotion(np.array([image]))]
            return emotion






            