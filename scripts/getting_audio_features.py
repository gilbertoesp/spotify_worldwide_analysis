""" Consiguiendo los features de los track_id """
import requests
import pandas as pd
import ast #string to dict

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQDu8CUSPu8V8xUQuwsA5ORFT9csbuFOiaEyvIcb4ZaCQCNkdnEVeGwkdEi1p3Icg7WU5NVewswjziUsavvZHHjFQJbQFOKWKbtohd6_VjeHU8n8MzVybfQQU7ZZfvB3fOlvYEXvTzXNrb2ruQyeTidobbyeXIedizzFJCW98ghrE_Hz2Y1x2_TddYf8KPk0cD8WmkV_OISH17zng881rqvD8ijc1vypAowDTwqha-MU10PIo8dV8ew3rYrl_M83ZzdJIH95lkMjNOgcgt_A',
    # OAuth Token Solicitar en la pagina y actualizar segun sea necesario
    # https://developer.spotify.com/console/get-audio-features-several-tracks/
}
# Pequeno dataset para probar script
df = pd.read_csv("data/data.csv")
df = df.dropna()

url_list = df['URL'].tolist() # conseguimos la lista de urls


tracks = [] # codigos de las canciones que vamos a conseguir sus features
for i,url in enumerate(url_list):
    #dividimos los url para extrar el track_id unico para cada cancion
    if pd.isnull(url):
        print("URL denegada: {}\t Index: {}".format(url, i))
    else:
        tracks.append(url.split('track/')[1])

print("Cantidad de URL a solicitar: {}".format(len(url_list)))

# juntamos todos los tracks en una sola string para mandar el requests
# pediremos los datos de 1000 en 1000

tracks_a_solicitar = ','.join(tracks[:])
#print("Solicitando tracks {} al {}".format(i,(i+1)*1000 + 1))
params = (
    ('ids', tracks_a_solicitar),
)
# Solicitando todos los features
try:
    response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print("error. Request Denegada")
    #sys.exit(1)

""" Pasamos los datos a una lista """
#print(response.text)
features_temp = ast.literal_eval(response.text)
# spotify regresa un diccionario raro, asi que lo limpiamos un poco
features = (features_temp['audio_features'])

print("Cantidad de feautures: {}".format(len(features)))
# dict con llaves track_id y valores sus features
#track_feature = {tracks[i]:features[i] for i in range(len(tracks))}

# pasando los features a un diccionario de lista
features_list = {}
for feature in features[0].keys():
    features_list[feature] = []
    for i in range(len(features)):
        features_list[feature].append(features[i][feature])
        # agregando las features a nuestro df
    df[feature] = features_list[feature]

#Guardamos todo en un bonito csv nuevo
df.to_csv('data/data_with_features.csv')
