import pandas as pd
from sklearn import linear_model 
from util.get_file_path import get_file_path
from util.read_raw_CSV import read_raw_CSV
import util.cleaners as clean
import util.split_data as split_data
import matplotlib.pyplot as plt
import numpy as np 

data_file = get_file_path("fitbit_export_20140710.csv")
[activity,sleep] = read_raw_CSV(data_file,["Activity","Sleep"])

x_raw = sleep['Minutes Awake'].values # convert dataframe to numpy array
y_raw = sleep['Minutes Asleep'].values
x,y = clean.zap_zeros(x_raw,y_raw)
x = clean.convert_to_matrix(x)
y = clean.convert_to_matrix(y)

test_frac = 0.15 # fraction of data to use for testing (training set fraction is 1 - test_frac)
#[x_train,y_train,x_test,y_test] = split_data.split_consec(x,y,test_frac)
[x_train,y_train,x_test,y_test] = split_data.split_rand(x,y,test_frac)

clf = linear_model.LinearRegression(fit_intercept=True)
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

plt.show()
