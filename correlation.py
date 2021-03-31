# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:13:22 2021

@author: Zakaria
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as st
dataset = pd.read_csv("iris.csv")

#sans regrssion
plot = sns.pairplot(dataset, kind="scatter")

plt.show()

dataset.head()
X_1, Y_1 = dataset["longueur_sepal"], dataset["largeur_sepal"]
cor_1 = st.pearsonr(X_1, Y_1)
print(cor_1)

X_2, Y_2 = dataset["longueur_petal"], dataset["largeur_petal"]
cor_2 = st.pearsonr(X_2, Y_2)
print(cor_2)