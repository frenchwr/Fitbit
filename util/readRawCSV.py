from util.getDays import getDays
from util.cleaners import cleanDataFrame
import pandas as pd
from sys import exit

def readRawCSV(csvFile,typeList):
    # I should write a little reader here that wraps getDays and read_csv:
    # [activity,sleep] = readRawDatafile(dataFile,["Activity","Sleep"])
    nrows = getDays(csvFile)
    skiprowsActivity = 1
    skiprowsSleep = nrows + 4
    output = []
    for theType in typeList:
        if ( theType is "Activity"):
            newType = pd.read_csv(csvFile,skiprows=skiprowsActivity,nrows=nrows,index_col=0)
            cleanDataFrame(newType)
            output.append(newType)
        elif ( theType is "Sleep" ):
            newType = pd.read_csv(csvFile,skiprows=skiprowsSleep,nrows=nrows,index_col=0)
            cleanDataFrame(newType)
            output.append(newType)
        else:
            print "Error: unsupported type: ",theType
            print "       Only Activity and Sleep currently supported"
            print "       Continuing to next type"
            continue
    
    if not output:
        print "Error: no valid types entered"
        exit()
        
        
    return output