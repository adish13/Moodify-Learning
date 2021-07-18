import base64
import requests
import datetime
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

auth_manager=SpotifyClientCredentials(client_id='a1b9d1bb257b422184ccdf717256c1e0',
client_secret='6f3679d7e3bb4591953e0ab88d8cc0c8')

sp=spotipy.Spotify(auth_manager=auth_manager)
ids=['6RUKPb4LETWmmr3iAEQktW', '0tgVpDi06FyKpA1z0VMD4v', '2r6OAV3WsYtXuXjvJ1lIDi']
df = pd.DataFrame(columns=['Name', 'Album', 'Artist', 'Release_date', 'Popularity', 'Acousticness', 'Danceability', 'Energy',
                                     'Instrumentalness', 'Liveness', 'Loudness',
                                     'Speechiness', 'Tempo', 'Time_signature', 'Valence', 'Length', 'Key', 'Mode'])
                                     
def give_data():
        df = pd.DataFrame(columns=['Name', 'Album', 'Artist', 'Release_date', 'Popularity', 'Acousticness', 'Danceability', 'Energy',
                                     'Instrumentalness', 'Liveness', 'Loudness',
                                     'Speechiness', 'Tempo', 'Time_signature', 'Valence', 'Length', 'Key', 'Mode'])
        for id in ids:
          track_info= sp.track(id)
          track_features = sp.audio_features(id)
          name= track_info['name']
          album = track_info['album']['name']
          artist = track_info['album']['name']
          release_date = track_info['album']['release_date']
          popularity= track_info['popularity']
          acousticness = track_features[0]['acousticness']
          danceability= track_features[0]['danceability']
          energy= track_features[0]['energy']
          instrumentalness= track_features[0]['instrumentalness']
          liveness= track_features[0]['liveness']
          loudness= track_features[0]['loudness']
          speechiness= track_features[0]['speechiness']
          tempo= track_features[0]['tempo']
          time_signature= track_features[0]['time_signature']
          valence= track_features[0]['valence']
          length= track_features[0]['duration_ms']
          key= track_features[0]['key']
          mode= track_features[0]['mode']
          track=[name, album, artist, release_date, popularity, acousticness,
               danceability, energy, instrumentalness, liveness, loudness,
               speechiness,tempo, time_signature, valence, length, key, mode]
          track
          df = df.append({
                          'Name':name, 'Album':album, 'Artist':artist, 'Release_date':release_date, 'Popularity':popularity,
                          'Acousticness':acousticness, 'Danceability':danceability, 'Energy':energy,
                                             'Instrumentalness':instrumentalness, 'Liveness':liveness, 'Loudness':loudness,
                                             'Speechiness':speechiness, 'Tempo':tempo, 'Time_signature':time_signature, 'Valence':valence,
                           'Length':length, 'Key': key, 'Mode':mode
                           }
                           ,ignore_index=True
                          )
        return df

