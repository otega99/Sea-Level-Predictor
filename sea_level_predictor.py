import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    x=pd.Series(list(range(1880,2051)))
    y=pd.Series(list(range(2000,2051)))
    # Create first line of best fit
    result=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(x,result.intercept + result.slope*x,'r')
    
    # Create second line of best fit
    new_df=df[df['Year']>1999]
    new_result=linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
    plt.plot(y,new_result.intercept + new_result.slope*y,'g')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()