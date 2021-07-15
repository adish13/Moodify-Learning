import cv2
from emotion_classify import emotion_detect
from music_test import recommend_music
import pandas as pd

def recommend(img_src, data_src):
    img = cv2.imread(img_src)
    mood = emotion_detect(img)
    data = pd.read_csv(data_src)
    recommend_music(data, mood)


img_src = input("Image link: ")
data_src = input("music source: ")

print(recommend(img_src, data_src))


