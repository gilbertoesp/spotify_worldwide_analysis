#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 02:11:16 2018

Este es mi archivo donde cargo mis funciones ya algo bien

@author: gilbertoesp
"""
#%%

#%%

def get_region(df, region):
    """
    Funcion que regresa el dataframe delimitado a una region
    """
    return df.loc[df['Region'] == region]

#%% DATES LIST
""" get dates dado un dataframe"""
def get_dates(df):
    """
        Regresa una lista de todas las fechas del df recibido.
        Las fechs estan en string foramto 2017-12-31
        No todos las regines tienen dias completos
    """
    dates = []
    for date in df['Date']:
        if date not in dates:
            dates.append(date)
    return dates
#%%
def get_top_by_day(num, date, df):
    """
    Regresa un dataframe con el top num de la fecha dada del df dado, asumimos el df 
    dado es de una region definida
    """
    return df.loc[df['Date'] == date].head(num)
#%% donde
def get_top(num, df, region=None, dates=None):
    """
        Regresa un dataframe que contiene el top num (e.g. top 10, top 50)
        de la region solicitada, y en un conjunto de fechas dada.
        region = {'mx','global', ...}
        date = ['20XX-12-31','20XX-12-31', ...]
    """
    if region is not None:
        df = get_region(df, region)
    if dates is None:
        dates = get_dates(df)
    
    data = pd.DataFrame()
    for date in dates:
        data = data.append(get_top_by_day(num, date, df))
        
    return data

#%%
""" TODO : diccionario de artistas dado un dataframe"""
def artists_frec(df):

    list_artists = df['Artist']#.tolist() # sera una lista de strings
    artist_frec = {}
    for artist in list_artists:
        if artist not in artist_frec:
            artist_frec[artist] = 1
        else:
            artist_frec[artist] += 1
    return artist_frec
#%%

#%%

#%%

#%%

#%%

