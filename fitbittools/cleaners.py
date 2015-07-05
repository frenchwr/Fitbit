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
        """Removes elements from dataframe with missing data"""
        return df[(df != 0).all(1)]

    def clean_dataframe(self,df):
        """Calls zap_zeros and remove_commas on a dataframe object"""
        self.remove_commas(df)
        return self.zap_zeros(df)
