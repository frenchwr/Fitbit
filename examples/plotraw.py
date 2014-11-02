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