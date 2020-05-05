# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:36:04 2020

@author: anony1
"""


##IRIS
import pandas 
from sklearn.datasets import load_iris
iris = load_iris()

import pandas as pd
pd.set_option('max_columns', 5)
pd.set_option('display.width', None)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = [iris.target_names[i] for i in iris.target]

iris_df.head()

pd.set_option('precision', 2)


import seaborn as sns
sns.set(font_scale = 1.1)
sns.set_style('whitegrid')
grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4],
                    hue='species')

import matplotlib.pyplot as plt


