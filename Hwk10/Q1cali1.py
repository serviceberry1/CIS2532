#
## Name:        Valerie Bixler
## Due Date:    Sunday, April 26, 2020
## Class:       CIS 2532-NET01  
## Pgm Name:    Hwk10PairPlot.py
##
## Assignment:  Create a Seaborn pairplot graph for the California
##              Housing dataset. 
##              
## Description: Program exercise 15.3 of Intro to Python for Computer
##              Science and Data Science by Paul Deitel, Harvey Deitel.
##              

#Import modules needed

from sklearn.datasets import fetch_california_housing

cali = fetch_california_housing()
print(cali.DESCR)
cali.data.shape
cali.target.shape
cali.feature_names
import pandas as pd
pd.set_option('precision', 4)
pd.set_option('max_columns', 9)
pd.set_option('max_columns', 9)
pd.set_option('display.width', None)
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df['MedHouseValue'] = pd.Series(cali.target)
cali_df.head()
sample_df = cali_df.sample(frac=0.1, random_state=17)
small_cali_df = cali_df[0:100]
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=2)
sns.set_style('whitegrid')
#for feature in cali.feature_names:
#    plt.figure(figsize=(16,9))
#    sns.scatterplot(data=sample_df, x=feature,
#    y='MedHouseValue', hue='MedHouseValue', 
#    palette='cool', legend=False)
    
#import seaborn as sns
#sns.set(font_scale = 1.1)
#sns.set_style('whitegrid')

#helpful:
#https://seaborn.pydata.org/generated/seaborn.pairplot.html
print('************************** Cali PairPlot follows ********') 
##FULL CHS data:  grid = sns.pairplot(cali_df)

gridSmall = sns.pairplot(small_cali_df)

plt.show()
#grid = sns.pairplot(data=cali_df, vars=cali_df.columns[0:9],
#                     hue='MedHouseValue')
#grid = sns.pairplot(data=cali_df, vars=cali_df.columns[0:4],
#                    hue='species')
#HEEHEE! RuntimeError: Selected KDE bandwidth is 0. Cannot estiamte density.
#Got past this runtime error by switching to just snspairplot(cali_df) w/o
#   parameeters
#Then wanted to run in Idle, so had to pip3 install scikit-learn again.
#Got matplotlib working with cali, but matplotlib doesn't allow zoom (tho
#  see the icons - believe it is due to my windows computer with cheap graphics card and
#  20,640 plotpoints of cali dataframe vs. Iris of 150 rows, 4 cols.
#
