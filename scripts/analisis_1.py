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
#==============================================================================
# SECCION CHEVERE
#==============================================================================    
    #%% Leyendo de pickle
    # diccionario con pos por region
    """ JUPYTER """
    # import pickle
    path = "data/"
    
    # diccionario con  las pos por region
    file_name = "region_range.dict"
    
    file_object = open(path+file_name,'rb')
    objeto = pickle.load(file_object)       #PICKLE
    region_range = objeto
    
    #%% Guardando datos en pickle
    """ JUPYTER """
    path = "data/"
    
    # diccionario con pos por region
    file_name = "region_range.dict"
    
    file_object = open(path+file_name, 'wb')
    pickle.dump(region_range, file_object)  #PICKLE
    file_object.close()
    
#==============================================================================
#     
#==============================================================================
    #%% Cargando datos
    daily_song_df = load("data.csv")
    #print(daily_song_df.head(10))
    
    
    #%%
#==============================================================================
#     #first_200 = daily_song_df["Track Name"][0:200]
#     
#     # Regresa objeto 'Index' poner atencion a el
#     columns = daily_song_df.columns
#         # Index(['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region'])
#     labels = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region']
#     # Seleccion columna sola - return Series
#     all_songs = daily_song_df["Track Name"]
#     
#     # Seleccion multiple columna - return DF
#     song_artist = daily_song_df[['Track Name','Artist','Streams']]
#     
#     
#==============================================================================
    
    #%%
    # Sortenado regiones
    #all_regions = daily_song_df['Region']
    
    #regiones = set()
    
    #for i in range(0,len(all_regions)):
    #    regiones.add(all_regions[i])
    
    # conjunto de todas las regiones con las que cuenta el df
    # print(regiones)

#==============================================================================
#     """
#      Contamos con 54 regiones, pues incluimos 'global', las canciones top del mundo.
#     """
#     global_list = list()
#     
#     for i in range(0,len(posiciones)):
#         if daily_song_df["Region"][i] == 'global':
#             global_list.append(i)
#     
#     len(global_list) # = 73800
#     
#     global_start, global_finish = min(global_list), max(global_list)
#     
#     global_df = daily_song_df[['Position', 'Track Name', 'Artist', 'Streams', 'Date', 'Region']][global_start:global_finish]
#     """
#     Conseguimos un dataframe con todos datos disponibles para la region 'global'
#     """
#==============================================================================
    #%%
    """ JUPYTER
        Conseguimos las posiciones del df que corresponden a las diferentes regiones
        Esta informacion se guardo en "data/region_range.dict" 
    """
    # todas las regiones
#==============================================================================
#     region_codigo = ['id', 'ca', 'sg', 'pt', 'au', 'hn', 'dk', 'pl', 'it', 'hk', 'ie', 
#                 'lt', 'gt', 'se', 'lu', 'fr', 'ar', 'ec', 'uy', 'tw', 'gr', 'do',
#                 'fi', 'co', 'global', 'lv', 'cz', 'at', 'bo', 'gb', 'jp', 'be', 
#                 'es', 'ee', 'no', 'nz', 'tr', 'br', 'is', 'pe', 'cr', 'mx', 'ch', 
#                 'pa', 'nl', 'hu', 'ph', 'sk', 'sv', 'cl', 'us', 'my', 'de', 'py']
#     region_nombre = ['Indonesia', 'Canada', 'Singapore', 'Portugal', 'Australia', 'Honduras', 'Denmark', 'Poland', 'Italy', 'Hong Kong','Irelad',
#                      'Lithuania', 'Guatemala','Senegal','Luxemburg','France','Argentina','Ecuador','Uruguay','Taiwan','Greece','Dominic Republic',
#                      'Finland','Colombia','Global','Latvia','Czech Republic','Austria','Bolivia','United Kingdom','Japon','Belgium',
#                      'Spain','Estonia','Norway','New Zeland','Turkey','Brazil','Iceland','Peru','Costa Rica','Mexico','Switzerland',
#                      'Panama', 'Netherlands', 'Hungary','Philippines', 'Slovakia', 'El Salvador', 'Chile', 'United States','Malaysia','Germany','Paraguay']
#     
#     regiones = {region_codigo[i]:region_nombre[i] for i in range(0,len(region_codigo))}
#==============================================================================
    regiones = {'id': 'Indonesia', 'ca': 'Canada', 'sg': 'Singapore', 'pt': 'Portugal', 
              'au': 'Australia', 'hn': 'Honduras', 'dk': 'Denmark', 'pl': 'Poland', 
              'it': 'Italy', 'hk': 'Hong Kong', 'ie': 'Irelad', 'lt': 'Lithuania', 
              'gt': 'Guatemala', 'se': 'Senegal', 'lu': 'Luxemburg', 'fr': 'France', 
              'ar': 'Argentina', 'ec': 'Ecuador', 'uy': 'Uruguay', 'tw': 'Taiwan', 
              'gr': 'Greece', 'do': 'Dominic Republic', 'fi': 'Finland', 'co': 'Colombia', 
              'global': 'Global', 'lv': 'Latvia', 'cz': 'Czech Republic', 'at': 'Austria', 
              'bo': 'Bolivia', 'gb': 'United Kingdom', 'jp': 'Japon', 'be': 'Belgium', 
              'es': 'Spain', 'ee': 'Estonia', 'no': 'Norway', 'nz': 'New Zeland', 
              'tr': 'Turkey', 'br': 'Brazil', 'is': 'Iceland', 'pe': 'Peru', 
              'cr': 'Costa Rica', 'mx': 'Mexico', 'ch': 'Switzerland', 
              'pa': 'Panama', 'nl': 'Netherlands', 'hu': 'Hungary', 'ph': 'Philippines',
              'sk': 'Slovakia', 'sv': 'El Salvador', 'cl': 'Chile', 'us': 'United States',
              'my': 'Malaysia', 'de': 'Germany', 'py': 'Paraguay'}

#============== region_range.dict -- PICKLE ========================================
     # rangos para todas las regiones
     region_range = dict() #un dict cuyas keys seran las regiones
 
     for region in regiones.keys():
         region_range[region] = list()
         
     for i in range(0, len(daily_song_df)): # region_range.dict - Guardado File
         region_range[ daily_song_df["Region"][i] ].append(i)
#==============================================================================

    # conseguimos cuantos registros hay en total para cada region
    region_total = dict()
    for region in region_range:
        region_total[region] = len(region_range[region])
        
    # guardamos estas cantidades en una lista para ver sus propiedades
    cantidad_registros = [region_total[region] for region in regiones.keys()]
    
    # Verificamos los registros
    sum(cantidad_registros)# == len(daily_song_df)
    max(cantidad_registros)
    min(cantidad_registros)
    """
       Notamos que el maximo es 74200, lo cual que si todos los dias estan completos con sus 200 registros
       contamos con 371 dias para estos casos. Mientras que en la peor region tenemos 4098 registros, de igual
       manera si estan las 200 canciones tendremos 20.49 dias de registros
    """
    # que regiones tienen maxima cantidad de registros 74200
    regiones_completas = {region:region_total[region] for region in regiones.keys() if region_total[region] == max(cantidad_registros)}
    # regiones que tienen menos datos, las que restan
    # ordenadas en un diccionario
    regiones_incompletas = {region:region_total[region] for region in regiones.keys() if region not in regiones_completas}
    ### {regiones[region]:region_total[region] for region in regiones_incompletas.keys()}
        
    
    #%%
    """ Conseguir un DataFrame por pais
        mx siendo el primero, dado el rango conseguido anteriormente y cargado por pickle
    """
    labels = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region']
    # MEXICO
    mx_range = region_range['mx']
    mx_df = daily_song_df.loc[mx_range[0]:mx_range[-1]]
    
    
    """ 
    Genera un dataframe en la region que querramos
    Tomo luxamburgo por ser la mas pequena
    Vemos que hay dia en las que solo hay un registro, un dia con una unica cancion en el
    top 200, segun avanza podemos ver mas registros por dia
    """
    region = 'lu'
    lu_df = daily_song_df.loc[region_range[region][0]:region_range[region][-1]]
    
    """ TODO
    Separar dataframe por fechas, cada dia
    """
    
    """ TODO
    Dataframe con el top 10 de cada pais
    """
    
    """ TODO
    Analizar regiones_incompletas
        dias faltantes
        intervalos de fechas
        por que faltan datos
        cuales faltan
    """
    
    