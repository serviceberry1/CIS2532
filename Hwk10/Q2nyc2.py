#
## Name:        Valerie Bixler
## Due Date:    Sunday, April 26, 2020
## Class:       CIS 2532-NET01  
## Pgm Name:    Hwk10LinRegress.py
##
## Assignment:  Simple Linear Regression with Average Yearly NYC
##              Temperature Time Series
##              
## Description: Program exercise 15.6 of Intro to Python for Computer
##              Science and Data Science by Paul Deitel, Harvey Deitel.
##              Reimplement the simple linear regression cast study of
##              Section 15.4 of the textbook using the file provided by
##              the teacher, and found at www.ncdc.noaa.gov/cag.
##
##              Answer the question:
##              How does the temperature trend compare to the average
##              January high temperatures?
##              

#Time Series and Simple Linear Regression p620 Deitel & Deitel
import pandas as pd
nyc = pd.read_csv('C:\\CIS2532\\Hwk10\\ave_yearly_temp_nyc_1895-2017.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']    #Rename Value col to Temperature
nyc.Date = nyc.Date.floordiv(100) 
nyc.head(3)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
nyc.Date.values.reshape(-1,1), nyc.Temperature.values, 
random_state=11)
#Confirm the 75% - 25% train-test split by checking shapes:
X_train.shape
X_test.shape
from sklearn.linear_model import LinearRegression
lin_regress = LinearRegression()
lin_regress.fit(X=X_train, y=y_train)
lin_regress.coef_
lin_regress.intercept_
predicted = lin_regress.predict(X_test)
expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')
    
#Predicting future temps and estimating past temps
predict = (lambda x: lin_regress.coef_ * x +
lin_regress.intercept_)
predict(2018)
predict(1890)
#Visualize the dataset w/the regression line
import seaborn as sns

axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', 
    hue='Temperature', palette='winter', legend=False)
##axes.set_ylim(10, 70)  #better shows lin regression line

import numpy as np
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)
import matplotlib.pyplot as plt
line = plt.plot(x, y) 
#Looks better if comment out the set_ylim above
#Shows scatterplot w/line of regress thru it


print('slope of avg yearly NYC: ', (y[1] - y[0]) / (x[1] - x[0]))

#To answer question 2, must go back to NOAA website and get Jan
#  data for NYC - make sure at top to go to CITY
#https://www.ncdc.noaa.gov/cag/city/time-series/USH00305801/tavg/1/1/1895-2017?base_prd=true&begbaseyear=1901&endbaseyear=2000
#from orig website:
#https://www.ncdc.noaa.gov/cag
#
#After plot it, then click excel button to download the .csv file
#  of your data.
#That data file named:
##############################################
nyc = pd.read_csv('C:\\CIS2532\\Hwk10\\ave_yearly_tempJAN_nyc_1895-2017.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']    #Rename Value col to Temperature
nyc.Date = nyc.Date.floordiv(100) 
nyc.head(3)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
nyc.Date.values.reshape(-1,1), nyc.Temperature.values, 
random_state=11)
#Confirm the 75% - 25% train-test split by checking shapes:
X_train.shape
X_test.shape
from sklearn.linear_model import LinearRegression
lin_regress = LinearRegression()
lin_regress.fit(X=X_train, y=y_train)
lin_regress.coef_
lin_regress.intercept_
predicted = lin_regress.predict(X_test)
expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')
    
#Predicting future temps and estimating past temps
predict = (lambda x: lin_regress.coef_ * x +
lin_regress.intercept_)
predict(2018)
predict(1890)
#Visualize the dataset w/the regression line
import seaborn as sns

axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', 
    hue='Temperature', palette='winter', legend=False)
##axes.set_ylim(10, 70)  #better shows lin regression line

import numpy as np
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)
import matplotlib.pyplot as plt
line = plt.plot(x, y) 

print('slope of January: ', (y[1] - y[0]) / (x[1] - x[0]))
plt.show()
#Looks better if comment out the set_ylim above
#Shows scatterplot w/line of regress thru it

#To answer question 2, must go back to NOAA website and get Jan
#  data for NYC - make sure at top to go to CITY
#https://www.ncdc.noaa.gov/cag/city/time-series/USH00305801/tavg/1/1/1895-2017?base_prd=true&begbaseyear=1901&endbaseyear=2000
#from orig website:
#https://www.ncdc.noaa.gov/cag
#
#After plot it, then click excel button to download the .csv file
#  of your data.
#That data file named:

