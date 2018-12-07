#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 01:19:42 2018

@author: gilbertoesp
"""

""" Cookbook """

""" Consiguiendo los features de los track_id """
import requests
import pandas as pd
import ast #string to dict

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer  BQCIUTTjHvvay3oQp6ZkreRjxs0Oh4PRM56_XZL1uy6siQjhGi8KgrfysHdh-e6W7iol3VLhsbL30KhjF1-o53LKkQEsAFJn_jtJRvg0-Tand_tzMlLW3Kvn5QoprK5RGZkacEoPj3mF8g8ix4zwfvSlpEayESxb0QGu-FYSnp4m0l2lhwsXtgv592SYTdPlA3TDxwXvu2aHQqlWoIcohuBPbNkbbvLxBI7oS5qJcnlnX_lP4o0GFkmJGjmLcswOwqWZNYAInPLeUEM0IZC_',
    # OAuth Token Solicitar en la pagina y actualizar segun sea necesario
    # https://developer.spotify.com/console/get-audio-features-several-tracks/
}
#%%
df = pd.read_csv("data/data.csv")
#df_features = pd.read_csv("data/features.csv")
df = df.dropna()
#%%
url_all = [set(df['URL'])]
unique_tracks = [url.split('track/')[1] for url in url_all]
# Canciones unicas

#%%

df_features = pd.DataFrame(data=None,columns = ['acousticness', 'analysis_url', 'danceability',
      'duration_ms', 'energy', 'id', 'instrumentalness', 'key', 'liveness',
      'loudness', 'mode', 'speechiness', 'tempo', 'time_signature',
      'track_href', 'type', 'uri', 'valence'])
start = 11400
step = 100
features = {}
for _ in range(25):
    tracks = unique_tracks[start:start+step]
    
    tracks_a_solicitar = ','.join(tracks)
    params = (
            ('ids', tracks_a_solicitar),
    )
    start = start + step
    try:
        response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("error. Request Denegada")
    
    #print(response.text)
    features_temp = ast.literal_eval(response.text)
    features_temp = features_temp['audio_features']
    # spotify regresa un diccionario raro, asi que lo limpiamos un poco
    
    #guardamos las features con en dict con valor id como keys
    for i in range(len(features_temp)):
        features[features_temp[i]['id']] = features_temp[i]

#1000
df_features = df_features.append(pd.DataFrame.from_dict(features, orient='index'))
df_features.to_csv("data/features.csv")
#==============================================================================
# df_features = pd.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 
#                                     'mode', 'speechiness', 'acousticness', 
#                                     'instrumentalness', 'liveness', 'valence',
#                                     'tempo', 'type', 'id', 'uri', 'track_href1576500', 
#                                     'analysis_url', 'duration_ms', 'time_signature'])
#==============================================================================
#%%
""" Escritura de features """
df_features = pd.read_csv('data/features_1_millon.csv')

id_all = list(df_features['id'])
id_unicos = []
for id in id_all:
    if id not in id_unicos:
        id_unicos.append(id)
        


#%%
""" Consiguiendo los datos del trabjo tonto de la semana pasada """
columns = ['acousticness', 'analysis_url', 'danceability',
      'duration_ms', 'energy', 'id', 'instrumentalness', 'key', 'liveness',
      'loudness', 'mode', 'speechiness', 'tempo', 'time_signature',
      'track_href', 'type', 'uri', 'valence']
features = {}

for track in unique_tracks:
    
    track_serie = df_features.loc['id' == track]
    track_dic = (dict(track_serie))
    features[track_dic['id']] = track_dic


#%% v3
start = 1578380
step = 20


df_features = pd.DataFrame(data=None,columns = ['acousticness', 'analysis_url', 'danceability',
      'duration_ms', 'energy', 'id', 'instrumentalness', 'key', 'liveness',
      'loudness', 'mode', 'speechiness', 'tempo', 'time_signature',
      'track_href', 'type', 'uri', 'valence'])
    
print(df_features)
#%%
start = 4600
step = 100
features = {}
for _ in range(100):
    tracks = unique_tracks[start:start+step]
    
    tracks_a_solicitar = ','.join(tracks)
    params = (
            ('ids', tracks_a_solicitar),
    )
    start = start + step
    try:
        response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("error. Request Denegada")
    
    #print(response.text)
    features_temp = ast.literal_eval(response.text)
    features_temp = features_temp['audio_features']
    # spotify regresa un diccionario raro, asi que lo limpiamos un poco
    
    #guardamos las features con en dict con valor id como keys
    for i in range(len(features_temp)):
        features[features_temp[i]['id']] = features_temp[i]

    
df_features = df_features.append(pd.DataFrame(features))
    
#%% v2
for index,row in df[20792:].iterrows():
    url = row['URL']
    track = url.split('track/')[1]
    params = (
            ('ids', track),
    )
    
    try:
        response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("error. Request Denegada")
    
    features_temp = ast.literal_eval(response.text)
    # spotify regresa un diccionario raro, asi que lo limpiamos un poco
    features = (features_temp['audio_features'])[0]

    df_features = df_features.append(features, ignore_index=True)
        
    #row['b'] = np.random.randint(0, 10)

#%% v1
#for i in range(len(df)/100):
    i = 0
    print("---------Iteracion {}-----------".format(i))
    sub_df = df[i*100:(i+1)*100] # 100 canciones por vuelta
    print("Consiguiendo canciones de {} a {}".format(i*100, (i+1)*100))
    url_list = sub_df['URL'].tolist()
    
    tracks = [] # codigos de las canciones que vamos a conseguir sus features
    for i,url in enumerate(url_list):
        #dividimos los url para extrar el track_id unico para cada cancion
        if pd.isnull(url):
            print("URL denegada: {}\t Index: {}".format(url, i))
        else:
            tracks.append(url.split('track/')[1])
            
    print("Cantidad de URL a solicitar: {}".format(len(url_list)))
    
    tracks_a_solicitar = ','.join(tracks[:])
    
    params = (
            ('ids', tracks_a_solicitar),
    )
    
    try:
        response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("error. Request Denegada")
        
    features_temp = ast.literal_eval(response.text)
    # spotify regresa un diccionario raro, asi que lo limpiamos un poco
    features = (features_temp['audio_features'])

    print("Cantidad de feautures: {}".format(len(features)))
    
    features_list = {}
    for feature in features[0].keys():
        features_list[feature] = []
    for i in range(len(features)):
        features_list[feature].append(features[i][feature])
        # agregando las features a nuestro sub df
    
    
    with open('data_with_features.csv', 'a') as f:
             sub_df.to_csv(f, header=True)   
    
    