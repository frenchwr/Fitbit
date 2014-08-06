import os
import inspect

def getFilePath(inputFile):
    scriptName = inspect.getframeinfo(inspect.currentframe()).filename
    scriptPath = os.path.dirname(os.path.abspath(scriptName))
    dataFile = scriptPath + "/../data/" + inputFile
    return dataFile