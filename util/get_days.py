from sys import exit

# Function for determing number of days we've collected data for
def get_days(file_name):
    n_rows = 0
    with open(file_name) as infile:
        for line in infile:
            if "-" in line:
                n_rows += 1
            elif "Sleep" in line:
                break
                
    if ( n_rows == 0 ):
        print "Error: unsupported fitbit data file format!"
        print "       expect date format: yyyy-mm-dd"
        exit()
        
    return n_rows
    