#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 01:11:40 2018

@author: gilbertoesp
"""

""" Clasificacion 1 - k-vecinos proximos """


#%%

# Inicializar el ambiente
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn import cluster # Auxiliar
import os
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

%matplotlib inline # ipython magic

#%%


