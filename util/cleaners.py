# Fitbit uses commas for val >= 1000 (i.e. 1,000),
# causing problems for parsing CSV files.
# This function removes the commas and converts to float
def cleanDataFrame(df):
    for c in df.columns:
        if (df[c].dtype == object):
            df[c] = df[c].str.replace(',','')
            df[c] = df[c].astype(float)