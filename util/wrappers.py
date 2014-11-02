import matplotlib.pyplot as plt
    

# A wrapper for plotting a pandas dataframe
def plotDataFrame(df,x=None,y=None,kind=None,startdate=None,enddate=None,stacked=False,gridsize=35,bins=15):
    
    if type(x) is str:
        x = [x] # convert string to list
    if type(y) is str:
        y = [y]
    
    if startdate is not None:
        df = df[startdate:]
    if enddate is not None:
        df = df[:enddate]
    
    # kind does not play nice when set to none, so need to define behavior for each plotting type
    
    if kind is 'bar' or kind is 'barh' or kind is 'area': df.plot(x=x,y=y,kind=kind,stacked=stacked)
    elif kind is 'hexbin': df.plot(x=x,y=y,kind=kind,gridsize=gridsize)
    elif kind is 'hist': df.plot(x=x,y=y,kind=kind,stacked=stacked,bins=bins)
    elif kind is 'box': df.plot(x=x,y=y,kind=kind)
    elif kind is 'scatter': df.plot(x=x,y=y,kind=kind)
    elif kind is 'pie': df.plot(x=x,y=y,kind=kind)
    else: df.plot(x=x,y=y)
    
    plt.show()