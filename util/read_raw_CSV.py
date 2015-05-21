from util.get_days import get_days
from util.cleaners import clean_data_frame
import pandas as pd
from sys import exit

def read_raw_CSV(csv_file,type_list):
    # I should write a little reader here that wraps getDays and read_csv:
    # [activity,sleep] = readRawDatafile(dataFile,["Activity","Sleep"])
	n_rows = get_days(csv_file)
	skip_rows_activity = 1
	skip_rows_sleep = n_rows + 4
	output = []
	for the_type in type_list:
		if ( the_type is "Activity" ):
			print(csv_file)
			print(skip_rows_activity)
			print(n_rows)
			new_type = pd.read_csv(csv_file,skiprows=skip_rows_activity,nrows=n_rows,index_col=0)
			print(new_type)
			clean_data_frame(new_type)
			output.append(new_type)
		elif ( the_type is "Sleep" ):
			print(csv_file)
			print(skip_rows_sleep)
			print(n_rows)
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