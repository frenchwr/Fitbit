import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import random

def get_poly_range(x,training_ids,testing_ids):
	# y = a + b*x + c*x^2
	poly = PolynomialFeatures(degree=2)
	# This returns a nsamples x 3 matrix, with
	# the first column set to 1 as there is no 
	# dependence on x for the a term. This is related
	# to why we use fit_intercept False in this example
	# but True in the linear regression example.
	x_poly = poly.fit_transform(x)
	x_train_poly = x_poly[training_ids]
	x_test_poly = x_poly[testing_ids]
	return x_train_poly,x_test_poly
	

def split_consec(x,y,frac,Poly=False):
	n_test = int (len(x) * frac)
	n_train = len(x) - n_test
	training_inds = range(0,n_train)
	test_inds = range(n_train,len(x))
	x_train = x[:-n_test] # all but last 
	x_test = x[-n_test:] # last ten values
	y_train = y[:-n_test]
	y_test = y[-n_test:]
	print "Training set size: ",n_train
	print "Test size: ",n_test
	print "Test data makes up: ",100.0*n_test/len(x)," % of all data"
	if not Poly:
		return x_train,y_train,x_test,y_test
	else:
		[x_train_poly,x_test_poly] = get_poly_range(x,training_inds,test_inds)
		return x_train,y_train,x_test,y_test,x_train_poly,x_test_poly


def split_rand(x,y,frac,Poly=False):
	n_test = int (len(x) * frac)
	n_train = len(x) - n_test
	training_inds = random.sample(range(0,len(x)),n_train)
	test_inds = []
	for ind in range(len(x)):
		if ind not in training_inds:
			test_inds.append(ind)
	x_train = x[training_inds]
	y_train = y[training_inds]
	x_test = x[test_inds]
	y_test = y[test_inds]
	print "Training set size: ",n_train
	print "Test size: ",n_test
	print "Test data makes up: ",100.0*n_test/len(x)," % of all data"
	if not Poly:
		return x_train,y_train,x_test,y_test
	else:
		[x_train_poly,x_test_poly] = get_poly_range(x,training_inds,test_inds)
		return x_train,y_train,x_test,y_test,x_train_poly,x_test_poly

