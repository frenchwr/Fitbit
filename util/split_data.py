import numpy as np

def split_consec(x,y,frac):
	n_test = int (len(x) * frac)
	x_train = x[:-n_test] # all but last 
	x_test = x[-n_test:] # last ten values
	y_train = y[:-n_test]
	y_test = y[-n_test:]
	print "Training set size: ",len(x_train)
	print "Test size: ",len(x_test)
	print "Test data makes up: ",100.0*len(x_test)/len(x)," % of all data"
	return x_train,y_train,x_test,y_test