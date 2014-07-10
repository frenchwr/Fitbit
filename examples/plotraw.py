import pandas as pd # 7/4/2014 -- installed version 0.14.0
import os
import inspect
from util.getDays import getDays
from util.cleaners import cleanDataFrame
from util.wrappers import plotDataFrame

# get path where this script is executed from
# I should wrap this up:
# dataFile = getFilePath("fitbit_export_20140710.csv")
scriptName = inspect.getframeinfo(inspect.currentframe()).filename
scriptPath = os.path.dirname(os.path.abspath(scriptName))
dataFile = scriptPath + "/../data/fitbit_export_20140710.csv"

# I should write a little reader here that wraps getDays and read_csv:
# [activity,sleep] = readRawDatafile(dataFile,["Activity","Sleep"])
nrows = getDays(dataFile)
skiprowsActivity = 1
skiprowsSleep = nrows + 4

activity = pd.read_csv(dataFile,skiprows=skiprowsActivity,nrows=nrows,index_col=0)
cleanDataFrame(activity)
sleep = pd.read_csv(dataFile,skiprows=skiprowsSleep,nrows=nrows,index_col=0)
cleanDataFrame(sleep)
# combine activity and sleep data
allData = pd.concat([activity,sleep])

# plotDataFrame tests:
# kind can be line, bar, barh, area, scatter, hexbin, pie 
# Note: Some of the plot types work with time series data only (time vs. var Y);
#       This includes line, bar, barh, and area.
# Note: Others plot types are designed to plot var X vs. var Y.
#       This includes scatter, hexbin, and pie.

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