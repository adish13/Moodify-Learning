import pprint
import sys
import os
import spotipy
import spotipy.util as util
import simplejson as json
import string
import random
import requests
import base64
import datetime
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
import streamlit as st

os.environ['SPOTIPY_CLIENT_ID']='f7a43754c96842d0abe4714b5d46b5b8'
os.environ['SPOTIPY_CLIENT_SECRET']='b220dc8a84284d15960df4b2460255ee'
os.environ['SPOTIPY_REDIRECT_URI']='http://127.0.0.1:8000/'

def get_token():
    username = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = 10))
    #  if len(sys.argv) > 1:
    #     username = sys.argv[1]
    #  else:
    #     print("Usage: %s username" % (sys.argv[0],))
    #     sys.exit()

    scope = ['user-library-read','user-read-recently-played','playlist-modify-private','playlist-modify-public','playlist-read-private','playlist-read-collaborative','user-read-private']

    token = util.prompt_for_user_token(
            username=username,
            scope=scope,
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"))
    if token:
        return token
    else:
        print("Can't find user token. Try again")

def fetch_username(token):
    uri = '	https://api.spotify.com/v1/me'
    req = requests.get(uri,headers={'Authorization': 'Bearer ' + str(token)})
    req = req.json()
    print(req)
    username = req['id']
    return username


def fetch_ids(token):
    if token:
        # print(token)
        # sp = spotipy.Spotify(auth=token)
        # sp.trace = False
        # results = sp.current_user_playlists(limit=50)
        # for i, item in enumerate(results['items']):
        #     print("%d %s" %(i, item['name']))
        # #user history
        uri = 'https://api.spotify.com/v1/me/player/recently-played'
        req = requests.get(uri,headers={'Authorization': 'Bearer ' + str(token)},params={'limit':50})
        data = req.json()
        ids = [data['items'][i]['track']['id'] for i in range(len(data['items']))]
        return ids
    else:
        print("Can't fetch user history")
        return []

def create_playlist(token, ids):
    username = fetch_username(token)
    sp = spotipy.Spotify(auth=token)
    time = datetime.datetime.now()
    playlist_name = f'Playlist by Moodify | {time.strftime(f"%m/%d/%Y, %H:%M:%S")}'   
    sp.user_playlist_create(username, name=playlist_name)
    print("Successfully created Playlist")
    
    playlist_id = ''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:  # iterate through playlists I follow
        if playlist['name'] == playlist_name:  # filter for newly created playlist
            playlist_id = playlist['id']

    sp.user_playlist_add_tracks(username, playlist_id, ids)
    return None

def make_df(token):
    
    auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))

    sp=spotipy.Spotify(auth_manager=auth_manager)
    ids=fetch_ids(token)
    df = pd.DataFrame(columns=['ID', 'Name', 'Album', 'Artist', 'Release_date', 'Popularity', 'Acousticness', 'Danceability', 'Energy',
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
                        'ID': id, 'Name':name, 'Album':album, 'Artist':artist, 'Release_date':release_date, 'Popularity':popularity,
                        'Acousticness':acousticness, 'Danceability':danceability, 'Energy':energy,
                                            'Instrumentalness':instrumentalness, 'Liveness':liveness, 'Loudness':loudness,
                                            'Speechiness':speechiness, 'Tempo':tempo, 'Time_signature':time_signature, 'Valence':valence,
                        'Length':length, 'Key': key, 'Mode':mode
                        }
                        ,ignore_index=True
                        )
    print(df)
    return df

if __name__ == "__main__":
    token = get_token()
    print(fetch_ids(token))
    print(token)

    