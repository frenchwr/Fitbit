import pandas as pd # 11/01/2014 -- installed version 0.15.0
from sklearn import linear_model # installed 11/01/2014, 0.15.2
from util.get_file_path import get_file_path
from util.read_raw_CSV import read_raw_CSV
from sklearn.preprocessing import PolynomialFeatures
from numpy.polynomial.polynomial import polyval
import util.cleaners as clean
import matplotlib.pyplot as plt
import numpy as np 

data_file = get_file_path("fitbit_export_20140710.csv")
[activity,sleep] = read_raw_CSV(data_file,["Activity","Sleep"])

x_raw = sleep['Minutes Awake'].values
y_raw = sleep['Minutes Asleep'].values
x,y = clean.zap_zeros(x_raw,y_raw)
x = clean.convert_to_matrix(x)
y = clean.convert_to_matrix(y)

# y = a + b*x + c*x^2
poly = PolynomialFeatures(degree=2)
# This returns a nsamples x 3 matrix, with
# the first column set to 1 as there is no 
# dependence on x for the a term. This is related
# to why we use fit_intercept False in this example
# but True in the linear regression example.
x_poly = poly.fit_transform(x)

# Break data up into training and test sets
n_test = 7
x_train = x[:-n_test] # all but last n_test values
x_test = x[-n_test:] # last n_test values
x_train_poly = x_poly[:-n_test]
x_test_poly = x_poly[-n_test:]
y_train = y[:-n_test]
y_test = y[-n_test:]
print "Training set size: ",len(x_train)
print "Test size: ",len(x_test)
print "Test data makes up: ",100.0*len(x_test)/len(x)," % of all data"

clf = linear_model.LinearRegression(fit_intercept=False)
clf.fit(x_train_poly, y_train)

# The coefficients
print "Coefficients: \n", clf.coef_[0]
# The mean square error, this result doesn't change as I toggle
# fit_intercept...seems 
print("Residual sum of squares: %.2f"
      % np.mean((clf.predict(x_test_poly) - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % clf.score(x_test_poly, y_test))

# Plot outputs
plt.scatter(x_test, y_test,  color='black')
x_regular = np.linspace(x_train.min(),x_train.max(),200)
y_regular_poly = polyval(x_regular, clf.coef_[0])
plt.plot(x_regular, y_regular_poly, color='blue',linewidth=3)

plt.show()