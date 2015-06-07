import numpy as np

class Cleaner:
    """Class for data cleaning utilities"""
    def __init__(self):
        pass

    def remove_commas(self,df):
        """Removes commas from fitbit dataframe"""
        for c in df.columns:
            if (df[c].dtype == object):
                df[c] = df[c].str.replace(',','')
                df[c] = df[c].astype(float)

    def zap_zeros(x,y):
        """Removes elements from numpy array with missing data"""
        zero_index_list = []
        for ind,val in enumerate(y):
            if val == 0: zero_index_list.append(ind)
        
        x_new = np.delete(x,zero_index_list)
        y_new = np.delete(y,zero_index_list)
        return x_new,y_new
