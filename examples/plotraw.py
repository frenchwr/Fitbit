import pandas as pd # 7/4/2014 -- installed version 0.14.0
from util.cleaners import cleanDataFrame
from util.wrappers import plotDataFrame

activity = pd.read_csv("/Users/Wilhelm/Desktop/fitbit_export_20140704.csv",skiprows=1,nrows=43,index_col=0)
cleanDataFrame(activity)
sleep = pd.read_csv("/Users/Wilhelm/Desktop/fitbit_export_20140704.csv",skiprows=47,nrows=43,index_col=0)
cleanDataFrame(sleep)
# combine activity and sleep data
allData = pd.concat([activity,sleep])

# plot data, kind can be line, bar, barh, area, scatter, hexbin, pie 
# Note: bar and barh try to cram all the tick labels onto the axis
# Note: scatter, hexbin, and pie require x and y data

# First test bar plots (time series data only)
plotDataFrame(sleep,y=['Minutes Asleep','Minutes Awake'],kind='bar',startdate='2014-06-03',enddate='2014-06-24',stacked=True)
plotDataFrame(sleep,y='Number of Awakenings',kind='barh',startdate='2014-06-03',enddate='2014-06-24')
# This should fail; only allow barplots when x is time
#plotDataFrame(sleep,x='Time in Bed',y=['Minutes Asleep','Minutes Awake','Number of Awakenings'],kind='bar',startdate='2014-03-01',enddate='2014-09-24')

# Test scatter plots (does not support time series figures, so must provide xdata)
plotDataFrame(sleep,x='Time in Bed',y=['Minutes Asleep','Minutes Awake','Number of Awakenings'],kind='scatter',startdate='2014-06-01',enddate='2014-06-24')
plotDataFrame(activity,x='Minutes Sedentary',y=['Minutes Very Active','Minutes Lightly Active'],kind='scatter')

# Test area plots (time series data)
plotDataFrame(sleep,kind='area',startdate='2014-06-01',enddate='2014-06-24')
plotDataFrame(activity,y=['Minutes Sedentary','Minutes Very Active','Minutes Lightly Active'],kind='area',stacked=False)
plotDataFrame(activity,y='Steps',kind='area')

# Test hexbin plotting (does not support time series figures, so must provide xdata)
plotDataFrame(sleep,x='Time in Bed',y='Minutes Asleep',kind='hexbin',startdate='2014-03-01',enddate='2014-08-24')
plotDataFrame(activity,x='Minutes Sedentary',y=['Minutes Lightly Active'],kind='hexbin')

# Test simple line plots (time series data)
plotDataFrame(sleep,kind='line',startdate='2014-06-01',enddate='2014-06-24')
plotDataFrame(activity,y=['Minutes Sedentary','Minutes Very Active','Minutes Lightly Active'],kind='line')
plotDataFrame(activity,y='Steps',kind='line')