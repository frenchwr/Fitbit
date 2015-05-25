import numpy as np
import random

def split_consec(x,y,frac):
	n_test = int (len(x) * frac)
	n_train = len(x) - n_test
	x_train = x[:-n_test] # all but last 
	x_test = x[-n_test:] # last ten values
	y_train = y[:-n_test]
	y_test = y[-n_test:]
	print "Training set size: ",n_train
	print "Test size: ",n_test
	print "Test data makes up: ",100.0*n_test/len(x)," % of all data"
	return x_train,y_train,x_test,y_test

def split_rand(x,y,frac):
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
	return x_train,y_train,x_test,y_test