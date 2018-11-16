#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:56:37 2018

@author: gilbertoesp
"""

import numpy as np
import pandas as pd
import os

df = pd.read_csv("data/data.csv")

#mx_data = df.loc[df['Region'] == 'mx'] # getting all mx data
#print(mx_data.head(10))
#
#print(mx_data.loc[mx_data['Date'] == '2017-01-01'][0:10]) # Conseguiendo datos por dia top 10
""" Formato de fechas 20XX-12-31 """

""" TODO : top 10 de cada dia """

#%% REGION DATAFRAME
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
def get_top(num, df):
    dates = get_dates(df)
    data = pd.DataFrame()
    for date in dates:
        data = data.append(get_top_by_day(num, date, df))
        
    return data
 #%%   
#=====================intento dos=========================================================
#     if dates is None:
#         dates = get_dates(df)
#         
#     top = df.loc[df['Date' == dates[0]]].head(num)
#     for date in dates[1:]:
#         next_top = df.loc[df['Date' == date].head(num)
#==============================================================================
    

#================intento uno==============================================================
#     """
#     Conseguimos el top num que se requiera
#     """
#     dates = get_dates(df)
#     # asumimos que le mandamos todo en orden
#     # df es el dataframe de una region
#     top = pd.DataFrame()
#     for date in dates:
#         top.append(df.loc[df['Date'] == date][0:num])
#         
#     return top
#==============================================================================

#%% MAIN
mx_data = get_region(df, 'mx')
mx_dates = get_dates(mx_data)

mx_top10 = get_top(10, mx_data)



