# Analisis inicial de Spotify Worlwide
# Manejare todo a traves de funciones

#%% BLOQUE DE FUNCIONES
import pandas as pd
import pickle
# Leyendo datos
def load(file):
    path = "data/" # se asume tenemos acceso a los datos
    path += file
    try:
        df = pd.read_csv(path)
        return df
    except:
        print("error al cargar de datos")
        
def get_df(df, column, value, labels):
    """
        Regresa un DataFrame, con la informacion que cumpla value en column
        
        df:     DataFrame a segmentar
        column: Columna que se busca
        value:  Valor que buscamos tenga la columna
        labels: Valores que queremos del DataFrame, dentro de estos se cumple
                la condicion value en column. list
    """
    value_list = list()
    for i in range(0,len(df)):    
        if(df[column] == value): #FIXME : ValueError: The truth value of a Series is ambiguous.
            value_list.append(i)
    
    return df[labels][min(value_list):max(value_list)]


#%% PLAYGROUND
if __name__ == "__main__":
    #%% Cargando datos
    daily_song_df = load("data.csv")
    #print(daily_song_df.head(10))
    
    
    #%%
    #first_200 = daily_song_df["Track Name"][0:200]
    
    # Regresa objeto 'Index' poner atencion a el
    columns = daily_song_df.columns
        # Index(['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region'])
    labels = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region']
    # Seleccion columna sola - return Series
    all_songs = daily_song_df["Track Name"]
    
    # Seleccion multiple columna - return DF
    song_artist = daily_song_df[['Track Name','Artist','Streams']]
    

    
    
    #%%
    # Sorteando posiciones
    posiciones = daily_song_df['Position']
    
    #lista_test = [i for i in range(1,201)] # [1,200]
    
    dias_completos = 0
    for j in range(0, len(posiciones)):
        if posiciones[j] == 200:
            dias_completos +=1
    # sum = 14402, la cantidad de que el 200 se encuentra en la lista, entonces
    # solo tenemos esta cantidad de dias completos,
    sum * 200 # = 2880400, canciones que estan en los dias completos
    
    
    
    
    #%%
    # Sortenado regiones
    #all_regions = daily_song_df['Region']
    
    #regiones = set()
    
    #for i in range(0,len(all_regions)):
    #    regiones.add(all_regions[i])
    
    # conjunto de todas las regiones con las que cuenta el df
    # print(regiones)
    regiones = ['id', 'ca', 'sg', 'pt', 'au', 'hn', 'dk', 'pl', 'it', 'hk', 'ie', 'lt', 'gt', 'se', 'lu', 'fr', 'ar', 'ec', 'uy', 'tw', 'gr', 'do', 'fi', 'co', 'global', 'lv', 'cz', 'at', 'bo', 'gb', 'jp', 'be', 'es', 'ee', 'no', 'nz', 'tr', 'br', 'is', 'pe', 'cr', 'mx', 'ch', 'pa', 'nl', 'hu', 'ph', 'sk', 'sv', 'cl', 'us', 'my', 'de', 'py']
    """
     Contamos con 54 regiones, pues incluimos 'global', las canciones top del mundo.
    """
    global_list = list()
    
    for i in range(0,len(posiciones)):
        if daily_song_df["Region"][i] == 'global':
            global_list.append(i)
    
    len(global_list) # = 73800
    
    global_start, global_finish = min(global_list), max(global_list)
    
    global_df = daily_song_df[['Position', 'Track Name', 'Artist', 'Streams', 'Date', 'Region']][global_start:global_finish]
    """
    Conseguimos un dataframe con todos datos disponibles para la region 'global'
    """
    # rangos para todas las regiones
    region_range = dict() #un dict cuyas keys seran las regiones

    for region in regiones:
        region_range[region] = list()
        
    for i in range(0, len(posiciones)):
        region_range[ daily_song_df["Region"][i] ].append(i)

#==============================================================================
#     #buscaremos en el dataframe todos lo datos que existan
#     for pos in range(0, len(daily_song_df)):
#         for region in regiones:
#             if daily_song_df["Region"][pos] == region:
#                 region_range[region].append(pos)
#                 break # si encuentra la region a la que pertenece terminamos
#         
# 
#==============================================================================
    # ==============================================================================
    # {'id', 'ca', 'sg', 'pt', 'au', 'hn', 'dk', 'pl', 'it', 'hk', 'ie', 'lt', 
    # 'gt', 'se', 'lu', 'fr', 'ar', 'ec', 'uy', 'tw', 'gr', 'do', 'fi', 'co', 
    # 'global', 'lv', 'cz', 'at', 'bo', 'gb', 'jp', 'be', 'es', 'ee', 'no', 'nz',
    # 'tr', 'br', 'is', 'pe', 'cr', 'mx', 'ch', 'pa', 'nl', 'hu', 'ph', 'sk', 'sv', 
    # 'cl', 'us', 'my', 'de', 'py'}
    
    
    #%% Guardando datos en pickle
    path = "data/"
    # diccionario con pos por region
    file_name = "region_range.dict"
    file_object = open(path+file_name, 'wb')
    
    pickle.dump(region_range, file_object)
    print("dumping")
    file_object.close()
    
    
    #%% Leyendo de pickle
    # diccionario con pos por region

    file_object = open(path+file_name,'rb')
    objeto = pickle.load(file_object)
    objeto == region_range
    #%%
    