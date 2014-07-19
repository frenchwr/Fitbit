import pandas as pd # 7/4/2014 -- installed version 0.14.0
import os
import inspect
from util.getDays import getDays
from util.cleaners import cleanDataFrame
from sklearn import linear_model # installed 7/18/2014, 0.15.0

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

clf = linear_model.LinearRegression()
