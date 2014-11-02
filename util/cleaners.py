import numpy as np

def clean_data_frame(df):
    # Fitbit uses commas for val >= 1000 (i.e. 1,000),
    # causing problems for parsing CSV files.
    # This function removes the commas and converts to float
    for c in df.columns:
        if (df[c].dtype == object):
            df[c] = df[c].str.replace(',','')
            df[c] = df[c].astype(float)
            
def convert_to_matrix(array):            
    # scikit-learn expects data in matrix format
    return np.reshape(array,(-1,1)) # convert to n x 1 matrix
            
def zap_zeros(x,y):
    
    zero_index_list = []
    for ind,val in enumerate(y):
        if val == 0: zero_index_list.append(ind)
        
    x_new = np.delete(x,zero_index_list)
    y_new = np.delete(y,zero_index_list)
    
    return x_new,y_new