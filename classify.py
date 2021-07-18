import cv2
from music_test import recommend_music


def recommend(mood, data):
    final_music_data=recommend_music(data, mood)
    return final_music_data



