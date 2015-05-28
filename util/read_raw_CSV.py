# You may get some errors if you are using
# pandas version 0.15, try updatig to 0.16+
from util.get_days import get_days
from util.cleaners import clean_data_frame
import pandas as pd
from sys import exit

def read_raw_CSV(csv_file,type_list):
	n_rows = get_days(csv_file)
	# careful with these next two lines if future Fitbit data exports
	# use a different format
	skip_rows_activity = 1 
	skip_rows_sleep = n_rows + 4
	output = []
	for the_type in type_list:
		if ( the_type is "Activity" ):
			new_type = pd.read_csv(csv_file,skiprows=skip_rows_activity,nrows=n_rows,index_col=0)
			clean_data_frame(new_type)
			output.append(new_type)
		elif ( the_type is "Sleep" ):
			new_type = pd.read_csv(csv_file,skiprows=skip_rows_sleep,nrows=n_rows,index_col=0)
			clean_data_frame(new_type)
			output.append(new_type)
		else:
			print "Error: unsupported type: ",the_type
			print "       Only Activity and Sleep currently supported"
			print "       Continuing to next type"
			continue
    
	if not output:
		print "Error: no valid types entered"
		exit()
        
        
	return output