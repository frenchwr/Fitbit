import matplotlib.pyplot as plt
from numpy import arange

class Plotter:
    """Class for plotting data"""
    def __init__(self):
        pass

    def plot_data_frame(self,df,x=None,y=None,kind=None,start_date=None,
                        end_date=None,stacked=False,figsize=None,
                        gridsize=35,bins=15):
        """Wrapper for plotting pandas data frame"""

        if type(x) is str:
            x = [x] # convert string to list
        if type(y) is str:
            y = [y]
    
        if start_date is not None:
            df = df[start_date:]
        if end_date is not None:
            df = df[:end_date]

        fsize = None
        if figsize != None:
            fsize = (12,8) # 12 x 8 inches, can make this more robust if needed

        # kind does not play nice when set to none, 
        # so need to define behavior for each plotting type
    
        if kind is 'bar' or kind is 'barh' or \
           kind is 'area': 
            ax = df.plot(x=x,y=y,kind=kind,stacked=stacked,figsize=fsize,rot=45)
            n = 5
            ticks = ax.xaxis.get_ticklocs()
            ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
            ax.xaxis.set_ticks(ticks[::n])
            ax.xaxis.set_ticklabels(ticklabels[::n])
        elif kind is 'hexbin': 
            df.plot(x=x,y=y,kind=kind,gridsize=gridsize,figsize=fsize)
        elif kind is 'hist': 
            df.plot(x=x,y=y,kind=kind,stacked=stacked,bins=bins,figsize=fsize)
        elif kind is 'box': 
            df.plot(x=x,y=y,kind=kind,figsize=fsize)
        elif kind is 'scatter': 
            df.plot(x=x,y=y,kind=kind,figsize=fsize)
        elif kind is 'pie': 
            df.plot(x=x,y=y,kind=kind,figsize=fsize)
        else: 
            df.plot(x=x,y=y,figsize=fsize)
    
        plt.show()
