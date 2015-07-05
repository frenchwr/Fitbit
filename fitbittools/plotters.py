import matplotlib.pyplot as plt
from numpy import arange,random

class Plotter:
    """Class for plotting data"""
    def __init__(self):
        pass

    def plot_multi_data(self,df,x,*args):
        """Plot multiple data sets on same figure"""
        fig,ax = plt.subplots()

        colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

        xnp = df[x].values
        ynp_list = [] # list of numpy arrays
        for ystring in args:
            ynp_list.append(df[ystring].values)

        maxyval = 0
        for ind,ynp in enumerate(ynp_list):
           color_ind = ind % len(colors)
           ax.plot(xnp,ynp,colors[color_ind]+'o',label=args[ind])
           if ( max(ynp) > maxyval ): maxyval = max(ynp)

        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        ax.set_ylim(0,1.1*maxyval)
        ax.set_xlabel(x,fontsize=16)
        ax.grid(color='k', linestyle='--', linewidth=0.3)
        fig.show()

    def plot_data_frame(self,df,x=None,y=None,kind=None,start_date=None,
                        end_date=None,stacked=False,figsize=None,
                        gridsize=35,bins=15,style=None):
        """Wrapper for plotting pandas data frame"""

        xstr = x 
        ystr = y
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
            ax = df.plot(x=x,y=y,kind=kind,gridsize=gridsize,figsize=fsize)
            ax.set_xlabel(xstr)
            ax.set_ylabel(ystr)
        elif kind is 'hist': 
            ax = df.plot(x=x,y=y,kind=kind,stacked=stacked,bins=bins,figsize=fsize)
        elif kind is 'box': 
            ax = df.plot(x=x,y=y,kind=kind,figsize=fsize)
            plt.xticks(rotation=45)
        elif kind is 'scatter': 
            #ax = df.plot(x=x,y=y,kind=kind,figsize=fsize,style=style)
            ax = df.plot(x=x,y=y,kind=kind,figsize=fsize,style=['o','rx'])
            ax.set_xlabel(xstr)
            ax.set_ylabel(ystr)
        elif kind is 'pie': 
            #df.plot(x=x,y=y,kind=kind,figsize=fsize)
            print("Fitbittools.plot_data_frame(): Pie charts aren't supported at the moment!")
            return
        else: 
            df.plot(x=x,y=y,figsize=fsize)
    
        plt.show()
