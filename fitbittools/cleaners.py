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

    def zap_zeros(self,df):
        """Removes elements from numpy array with missing data"""
        return df[(df.T != 0).any()]
