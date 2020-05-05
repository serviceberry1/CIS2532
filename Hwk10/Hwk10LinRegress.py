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
##              Reimplement the simple linear regression case study of
##              Section 15.4 of the textbook using the file provided by
##              the teacher, and found at www.ncdc.noaa.gov/cag.
##
##              Given a collection of numeric values representing an
##              independent variable and a dependent variable, simple
##              linear regression describes the relationship between
##              these variables w/a straight line, known as the
##              regression line.
##
##              Seek to answer this question using linear regression:
##              How does the temperature trend compare to the average
##              January high temperatures?
##              

#Import modules needed

import pandas as pd

#Use the LinearRegression estimator from sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Seaborn is a Python data visualization library based on matplotlib.
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#Describe what program does and ask for input data files.
def intro():
    print("\nSIMPLE LINEAR REGRESSION WITH AVERAGE YEARLY NYC TEMPERATURE TIME SERIES")
    print("\nThis program demonstrates simple linear regression using datasets ")
    print("  found at https://www.ncdc.noaa.gov/cag. The datasets are time series data")
    print("  for the New York City average annual temperatures from 1895 thru 2017.")          
    print("\nPlease enter the following 2 datasets so the data can be used to ")
    print("  produce a linear regression data visualization AND answer the question:")
    print("How does the temperature trend compare to the average January high temperatures?")
    print("\nFilepath example: C:\\CIS2532\\Hwk10\\ave_yearly_temp_nyc_1895-2017.csv")
    infileNYC = input("\nPlease enter average annual temperatures file: \n")
    infileJan = input("\nThanks! Now the JANUARY temperatures file: \n")
    print("\nStay tuned for the data visualization...\n")

    #return the datafiles.
    return infileNYC, infileJan


#Using input files, produce simple linear regression lines/scatterplots of data.
def simpleLinRegress(infile):

    #Get files of yearly NYC data, and January NYC data
    #nyc = pd.read_csv('C:\\CIS2532\\Hwk10\\ave_yearly_temp_nyc_1895-2017.csv')
    nyc = pd.read_csv(infile)

    #Names of .csv ds are Date(ccyymm), Value (##.#), Anomaly (-##.#)
    #  Rename Value column to Temperature
    nyc.columns = ['Date', 'Temperature', 'Anomaly']

    
    #Time Series and Simple Linear Regression pg620 Deitel & Deitel
    nyc.Date = nyc.Date.floordiv(100) 
    nyc.head(3)

    #Use the LinearRegression estimator.
    #We selected one column from the 2-dim DataFrame, resulting in a
    #  1-dim Series. However, scikit-learn estimators require their
    #  training and testing data to be 2-dim arrays, so use reshape
    #  method to do this.
    X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1,1), nyc.Temperature.values, 
    random_state=11)

    #Confirm the 75% - 25% train-test split by checking shapes:
    X_train.shape
    X_test.shape

    #Training the Model
    #Scikit-learn does not have a separate class for simple linear
    #  regression bc it's a special case of multiple linear regression,
    #  so need to train a LinearRegression estimator w/following lines:
    #Will use the 'from sklearn.linear_model import LinearRegression' here.
    lin_regress = LinearRegression()
    lin_regress.fit(X=X_train, y=y_train)

    #Get the slope and intercept used in the y = mx + b calc to make
    #  predictions. Slope is stored in estimator's coeff_ attrib
    #  (m in equation) and intercept is stored in estimator's
    #  intercept_ attrib (b in the equation).
    lin_regress.coef_
    lin_regress.intercept_

    #Testing the Model
    #Display predicted and expected values for every 5th element.
    predicted = lin_regress.predict(X_test)
    expected = y_test

    #for p, e in zip(predicted[::5], expected[::5]):
    #    print(f'predicted: {p:.2f}, expected: {e:.2f}')
        
    #Predicting future temps and estimating past temps
    predict = (lambda x: lin_regress.coef_ * x +
    lin_regress.intercept_)

    predict(2018) #bc end dataset 2017
    predict(1890) #bc prior to start of dataset

    #Visualize the dataset w/the regression line
    #Will use the imported seaborn here

    axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', 
        hue='Temperature', palette='winter', legend=False)
    ##axes.set_ylim(10, 70)  #better shows linear regression line
    ##Later it looked better when commented out the  set_ylim above


    #
    #Will use the imported numpy as np here to display
    #  the regression line
    #Create an array containing the min and max date values.
    #  These are the x-coords of the regression line's start
    #  and end points.
    x = np.array([min(nyc.Date.values), max(nyc.Date.values)])

    #Pass the array to the predict lambda producesan array w/
    #  corresponding predicted vals, which will be the y-coords.
    y = predict(x)

    #Will use the imported matplotlib.pyplot as plt here
    #  to plot a line based on the x and y arrays, which 
    #  represent the x and y coords of the points, respectively.
    #Displays scatterplot w/line of regression thru it.    
    line = plt.plot(x, y) 


    #Remebering slope as rise over run, caculated this using the
    #  data to make sure of results and help to describe.
    slope = (y[1] - y[0]) / (x[1] - x[0])
    print('\nSlope of file: ', infile)
    print('  is: ', slope )

    return slope


#Ask for input files, call functions to produce simple linear regression
#  lines, and calculate slope to verify what visualizations represent.
def main():

    try:                 #Use try/except to handle error processing.

        #Explain program to user and ask for input files 
        infileNYC, infileJan = intro()
        
        #Calculate and draw simple linear regression with avg annual NYC data.
        slopeNYC = simpleLinRegress(infileNYC)

        #To answer question 2, must go back to NOAA website and get Jan
        #  data for NYC - make sure at top to go to CITY
        #https://www.ncdc.noaa.gov/cag/city/time-series/USH00305801/tavg
        #    /1/1/1895-2017?base_prd=true&begbaseyear=1901&endbaseyear=2000
        #from orig website:  https://www.ncdc.noaa.gov/cag
        #After plot it, then click excel button to download the .csv file
        #  of your data.
        #Calculate and draw simple linear regression with avg NYC January data.        
        slopeJan = simpleLinRegress(infileJan)

        print("\nThe NYC average annual temps simple linear regression line is on the top,")
        print("the linear regression line for average January high temperatures below it.")
        if float(slopeNYC) > float(slopeJan):
            print("\nThe New York City average annual temperatures are rising faster ")
            print("than the average January high temperatures for NY City.")
        else:
            print("\nThe New York City average annual temperatures are rising slower ")
            print("than the average January high temperatures for NY City.")            


        #Print the scatter plot with the line of regression through it.
        plt.show()

        
        
    #except handles errors with file sizes causing index errors
    except IndexError:
        print('There was an indexing error!')

    #except handles keyboard interrupt error (or ctrl-c)
    except KeyboardInterrupt:
        print('Keyboard Interrupt!')

    #this except handles errors the previous do not, and prints error msg why.
    except Exception as err:
        print('An error occurred!')
        print(err)

    #else suite executes if NO exceptions raised.
    # If no exceptions raised, print the 'program complete' message and exit.
    else:    
        print("\nProgram has completed, Goodbye.")

    # finally suite executes to cleanup any files, etc. Finally execs no matter what,
    #  even if try AND exceptions raised. 
    #finally:


#Perform main function to run program.   
main()

