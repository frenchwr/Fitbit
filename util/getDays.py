from sys import exit

# Function for determing number of days we've collected data for
def getDays(filename):
    nrows = 0
    with open(filename) as infile:
        for line in infile:
            if "-" in line:
                nrows += 1
            elif "Sleep" in line:
                break
                
    if ( nrows == 0 ):
        print "Error: unsupported fitbit data file format!"
        print "       expect date format: yyyy-mm-dd"
        exit()
        
    return nrows
    