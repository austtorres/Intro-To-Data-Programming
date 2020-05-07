import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
These methods are designed to summarize a set of characteristics from the NOAA
dataset collection for a fixed time period. The data I chose to create a csv file
for is the daily amount of precipitation in inches for the month of May in 2012.
This code creates three different representations of the same data subset

Additional comment block: I chose to display a line, scatter, and bar chart. The
scatter plot contains a line of best fit to show trends that may help the viewer,
but it is not very useful for noticing.I chose a line graph because many days had
0 rain and the values are so small, so a line graph can show trends on a day-to
-day basis. The veiwer can follow the lines to see peaks and valleys of rainy
and dry periods of time. A bar chart does much better at showing the exact
amount of rain on each day compared to the next day.
The bar chart makes it more noticable that rain occurs mainly at the beginning
and end of the month.
    I have included that the middle of the month had little to no rain for most
days while the first and last third of each month showed much more rain.
I also concluded that bar charts are the most useful for displaying the data
that I chose to analyze.

**in Atom, only two graphs would display at once and the second graph would
combine the second and third graphs onto one chart. To fix this, I made separate
methods for each graph so that you can call each graph one by one. This makes
each graph display correctly**
"""



"""
The following code will create a scatter plot of the values for precipitation
per day in Madison county in May 2012. The trend of the scattered dots can be
described by a line of best fit. This line determines if rainfall increases,
decreases, or stays even based throughout the month based on its slope.
"""
def scatter(csvfile):
    #get data from csv
    df = pd.read_csv(csvfile)
    #set x axis
    x = df['DAY']
    #Set y axis
    y = df['PRECIPITATION']
    A1 = np.vstack([x,np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A1, y)[0]
    #plot data from csv
    df.plot.scatter('DAY','PRECIPITATION', title = 'Madison, WI precipitation totals (in inches) for May 2012')
    #creates line of best fit
    plt.plot(x, m*x+b)
    #show plot
    plt.show()


"""
The following code will create a line graph of the values for precipitation
per day in Madison county in May 2012. A line connects each point on the scatter
plot to display peaks and valleys as well as show upward or downward trends in
rainfall on a day-to-day basis.
"""
def line(csvfile):
    #get data from csv
    df = pd.read_csv(csvfile)
    #set x axis
    x = df['DAY']
    #Set y axis
    y = df['PRECIPITATION']
    df.plot('DAY', 'PRECIPITATION', label = 'Madison, WI precipitation in inches for May 2012')
    plt.show()


"""
The following code creates a bar chart for precipitationper day in Madison
county in May 2012. The bars make it easy to compare the magnitude of rainfall
between any given days. It also looks very clean and displays the data in a way
that makes it easy to see which part of the month experiences the most rain or
the least.
"""
def bar(csvfile):
    #get data from csv
    df = pd.read_csv(csvfile)
    #set x axis
    x = df['DAY']
    #Set y axis
    y = df['PRECIPITATION']
    ax = df['PRECIPITATION'].plot(kind='bar', title = "Madison, WI precipitation in inches for May 2012")
    #set label for x-axis
    ax.set_xlabel("Day of month")
    #set label for y-axis
    ax.set_ylabel("Precipitation in inches")
    #show data plots
    plt.show()
