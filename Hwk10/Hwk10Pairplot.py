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
##              Pairplot plots pairwise the relationships in a dataset.
##              Helpful:
##              https://seaborn.pydata.org/generated/seaborn.pairplot.html
##
##              By default, pairplot will create a grid of Axes such that each
##              numeric variable in data will by shared in the y-axis across a
##              single row and in the x-axis across a single column. The diagonal
##              Axes are treated differently, drawing a plot to show the univariate
##              distribution of the data for the variable in that column.
##

#Import modules needed
from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Describe what program does.
def intro():
    print("\nSEABORN PAIRPLOT GRAPH FOR THE CALIFORNIA HOUSING DATASET.")
    print("\nThis program demonstrates a pairplot graph for the California Housing ")
    print("  dataset that is fetched within the program from the sklearn.datasets")
    print("  so there is no need for a dataset to be input by the user.")          
    print("\nSeaborn's pairplot function creates a grid of scatter plots showing ")
    print("  features against one another. ")

    print("\nNote:  The pairplot diagrams work well for a small number of features")
    print("    or a subset of features, so that there is a small number of rows and")
    print("    columns and for a small number of samples so one can see the data ")
    print("    points. As the number of features and samples increase, the scatter")
    print("    plots quickly become almost too small to read.")

    print("\nStay tuned for the data visualization...")    

def pairPlot():

    #Fetch the California housing dataset
    cali = fetch_california_housing()
    #print(cali.DESCR)
    cali.data.shape
    cali.target.shape
    cali.feature_names

    #Here is where import pandas as pd
    pd.set_option('precision', 4)
    pd.set_option('max_columns', 9)
    pd.set_option('max_columns', 9)
    pd.set_option('display.width', None)

    #Create the DataFrame of California housing data
    cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
    cali_df['MedHouseValue'] = pd.Series(cali.target)
    cali_df.head()

    #Create a much small DataFrame to try and improve speed/ability
    #  to min/max windows.
    sample_df = cali_df.sample(frac=0.1, random_state=17)
    small_cali_df = cali_df[0:100]
    #Here is where need matplotlib.pyplot as plt
    #Here is where need seaborn as sns
    sns.set(font_scale=2)
    sns.set_style('whitegrid')

    #Commented this out because it took forever to run, so
    #  changed to use a much smaller dataset (small_cali_df).
    
    #Show different levels of a categorical variable by the
    #  color of plot elements with hue
    #
    #for feature in cali.feature_names:
    #    plt.figure(figsize=(16,9))
    #    sns.scatterplot(data=sample_df, x=feature,
    #    y='MedHouseValue', hue='MedHouseValue', 
    #    palette='cool', legend=False)
        
    #import seaborn as sns
    #sns.set(font_scale = 1.1)
    #sns.set_style('whitegrid')

    ##FULL CHS data:  grid = sns.pairplot(cali_df)
    
    #PairPlot
    #Note: the pairplot diags work well for a small num of features or
    #  a subset of features, so that there is a small num of rows & cols
    #  & for a small num of samples so can see the data points. As the
    #  num of features and & samples increase, the scatter plot quickly
    #  becomes too small to read.
    gridSmall = sns.pairplot(small_cali_df)

    #Display scatter plots of pairplot function.
    plt.show()
    

#Describe pairplot pgm and provide data visualization.
def main():

    try:                 #Use try/except to handle error processing.

        #Describe program 
        intro()

        #Go to pairPlot to produce Seaborn pairplot of data 
        pairPlot()
        
        
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

