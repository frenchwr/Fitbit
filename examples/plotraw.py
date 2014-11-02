from util.getFilePath import getFilePath
from util.readRawCSV import readRawCSV
from util.wrappers import plotDataFrame

dataFile = getFilePath("fitbit_export_20140710.csv")
[activity,sleep] = readRawCSV(dataFile,["Activity","Sleep"])
#allData = pd.concat([activity,sleep])

# 11/02/2014
# I spent a lot of time previously optimizing the layout of the axis and tick labels
# but when I updated all my python pacakges several months later everything was 
# broken...I'm just going to keep these plotting wrappers very minimal from now
# on and update the aestetics if I really need to

plotDataFrame(activity) # default kind is line
plotDataFrame(sleep,kind='bar',stacked=True)
plotDataFrame(activity,kind='area')
plotDataFrame(activity,x='Minutes Sedentary',y='Minutes Very Active',kind='hexbin')
plotDataFrame(sleep,kind='hist',stacked=True)
plotDataFrame(activity,kind='box')
plotDataFrame(activity,y=['Minutes Very Active','Minutes Lightly Active'],kind='pie')
plotDataFrame(sleep,x='Minutes Asleep',y='Minutes Awake',kind='scatter')
#activity.plot()
#plt.show()
#sleep.plot()
#plt.show()
#plotDataFrame(sleep,y=['Minutes Asleep','Minutes Awake'],kind='bar',startdate='2014-06-03',enddate='2014-06-24',stacked=True)
#plotDataFrame(sleep,y='Number of Awakenings',kind='barh',startdate='2014-06-03',enddate='2014-06-24')
# This should fail; only allow barplots when x is time
#plotDataFrame(sleep,x='Time in Bed',y=['Minutes Asleep','Minutes Awake','Number of Awakenings'],kind='bar',startdate='2014-03-01',enddate='2014-09-24')

# Test scatter plots (does not support time series figures, so must provide xdata)
#plotDataFrame(sleep,x='Time in Bed',y=['Minutes Asleep','Minutes Awake','Number of Awakenings'],kind='scatter',startdate='2014-06-01',enddate='2014-06-24')
#plotDataFrame(activity,x='Minutes Sedentary',y=['Minutes Very Active','Minutes Lightly Active'],kind='scatter')

# Test area plots (time series data)
#plotDataFrame(sleep,kind='area',startdate='2014-06-01',enddate='2014-06-24')
#plotDataFrame(activity,y=['Minutes Sedentary','Minutes Very Active','Minutes Lightly Active'],kind='area',stacked=False)
#plotDataFrame(activity,y='Steps',kind='area')

# Test hexbin plotting (does not support time series figures, so must provide xdata)
#plotDataFrame(sleep,x='Time in Bed',y='Minutes Asleep',kind='hexbin',startdate='2014-03-01',enddate='2014-08-24')
#plotDataFrame(activity,x='Minutes Sedentary',y=['Minutes Lightly Active'],kind='hexbin')

# Test simple line plots (time series data)
#plotDataFrame(sleep,kind='line',startdate='2014-06-01',enddate='2014-06-24')
#plotDataFrame(activity,y=['Minutes Sedentary','Minutes Very Active','Minutes Lightly Active'],kind='line')
#plotDataFrame(activity,y='Steps',kind='line')