
import requests # curl
import ast # string to dict
import pandas as pd
# Solicitud Spotify API
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAB9nAJkahto-xc6DnLCXLijEX1rcCUCN4DXUwE53xqjUy0ltivO7DdoLVEZ7TWclpwZIt56P-9L5Z-WX2kUQp3g3T8toSnlNhtWsKQ8sJzp1JLLr-vOC9oB88-KelzMHInC9spxoneOT-o0nMAI6IaznVLnFqzzbiv7Nz6WU7Wjau3PabNRVIq8-DP5V9m7pjj-ETO38_ysXe-encV5r-YPmrw1_ry4WmWsEt1EvgRTQ9XZmIl8bYEpStgzifWoZkp71H7f_9iORUEEcSR',
}
# URL
url = 'https://api.spotify.com/v1/audio-features/'

# tracks a cosneguir
#track = '11dFghVXANMlKmJXsNCbNl'
df = pd.read_csv("data/top50_ec.csv")
url_list = df['URL'].tolist()

tracks = []
for url in url_list:
    #dividimos los url para extrar el track_id unico para cada cancion
    tracks.append(url.split('track/')[1])

for track in tracks:
    solicitud = url + track
    response = requests.get(solicitud, headers=headers)

# print(response.text) # raw data en string

# diccionario con nuestras  caracteristicas de audio
    audio_f = ast.literal_eval(response.text)

# creamos un diccionario key : id track  y caracteristicas
    track_feautures = {}
    track_feautures[track] = audio_f
