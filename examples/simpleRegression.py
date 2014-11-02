import pandas as pd # 7/4/2014 -- installed version 0.14.0
#import os
#import inspect
from util.getFilePath import getFilePath
from util.readRawCSV import readRawCSV
from sklearn import linear_model # installed 7/18/2014, 0.15.0
#import matplotlib.pyplot as plt
#import numpy as np 

dataFile = getFilePath("fitbit_export_20140710.csv")
[activity,sleep] = readRawCSV(dataFile,["Activity","Sleep"])
allData = pd.concat([activity,sleep])

clf = linear_model.LinearRegression()

#sleep,x='Time in Bed',y='Minutes Asleep'
#df[df.c > 0.5][['b', 'e']].values
x = sleep['Time in Bed'].values
y = sleep['Minutes Asleep'].values

clf.fit(x, y)

# The coefficients
#print('Coefficients: \n', clf.coef_)
# The mean square error
#print("Residual sum of squares: %.2f"
#      % np.mean((clf.predict(x) - y) ** 2))
# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % clf.score(x, t))

# Plot outputs
#plt.scatter(x, y,  color='black')
#plt.plot(x, clf.predict(x), color='blue',
#         linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()
