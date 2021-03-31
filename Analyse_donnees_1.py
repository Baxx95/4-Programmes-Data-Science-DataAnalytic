# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:52:38 2021

@author: Zakaria
"""

import pandas as pd


dataset = pd.read_csv("tendance_centrale.csv")
#la moyenne
print(dataset.mean())

#la mediane
print(dataset.median())

#permet d'avoir la ou les valeur(s) la(les) plus représentative(s)
print(dataset.mode())

#Ecartype 
print(dataset.std())

#la symétrie
print(dataset.skew())

