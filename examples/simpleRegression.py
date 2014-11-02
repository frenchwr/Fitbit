import pandas as pd # 11/01/2014 -- installed version 0.15.0
from sklearn import linear_model # installed 11/01/2014, 0.15.2
from util.getFilePath import getFilePath
from util.readRawCSV import readRawCSV
import util.cleaners as clean
import matplotlib.pyplot as plt
import numpy as np 

dataFile = getFilePath("fitbit_export_20140710.csv")
[activity,sleep] = readRawCSV(dataFile,["Activity","Sleep"])
allData = pd.concat([activity,sleep])

x_raw = sleep['Minutes Awake'].values
y_raw = sleep['Minutes Asleep'].values
x,y = clean.zap_zeros(x_raw,y_raw)
x = clean.convert_to_matrix(x)
y = clean.convert_to_matrix(y)

# Break data up into training and test sets
n_test = 7
x_train = x[:-n_test] # all but last ten values
x_test = x[-n_test:] # last ten values
y_train = y[:-n_test]
y_test = y[-n_test:]
print "Training set size: ",len(x_train)
print "Test size: ",len(x_test)
print "Test data makes up: ",100.0*len(x_test)/len(x)," % of all data"

clf = linear_model.LinearRegression()
clf.fit(x_train, y_train)

# The coefficients
print "Coefficients: \n", clf.coef_
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((clf.predict(x_test) - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % clf.score(x_test, y_test))

# Plot outputs
plt.scatter(x_test, y_test,  color='black')
plt.plot(x_train, clf.predict(x_train), color='blue',
         linewidth=3)

#plt.xticks(())
#plt.yticks(())

plt.show()
