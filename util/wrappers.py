import matplotlib.pyplot as plt
from numpy import arange

# This is a helper function for plotDataFrame()
# It decides whether to include a legend or y-axis label           
def definePlotLabels(ax,y,kind):
    # make sure that y is a list of strings
    if ( len(y) > 1 ):
        ax.set_ylabel("")
        leg = plt.legend(loc='best')
        if kind is 'area':
            for l in leg.legendHandles:            
                l.set_linewidth(10)
    else:
        if ( kind is 'barh' ):
            ax.set_xlabel(y[0],fontsize=24)
        else:
            ax.set_ylabel(y[0],fontsize=24)
    

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
        
    return
    
    #fig, ax = plt.subplots()
    #colors = ['r', 'b', 'g', 'm', 'c', 'k']
    
    #if kind is 'bar' or kind is 'barh':
        
    #    if ( x is not None ):
    #        print 'plot not generated: bar plot only supports time series plotting'
    #        return
    #    if ( y is None ):
    #        df.plot(rot=25,kind=kind,stacked=stacked)
    #    else:
    #        print "Hello!"
    #        #df.plot(y=y,rot=25,kind=kind,stacked=stacked)
    #        #df.plot(y=y,kind=kind)
    #        df.plot(y='Minutes Asleep',kind='bar')
            
        #definePlotLabels(ax,y,kind)
    #    indices = arange(0,len(df.index),len(df.index)/5)
    #    print indices
    #    if kind is 'bar':
    #        print "Just passing through..."
    #        #ax.set_xticks( indices )
    #        #ax.set_xticklabels( df.index[indices] )
    #        pass
    #    else:
    #        ax.set_yticks( indices )
    #        ax.set_yticklabels( df.index[indices] )
    #elif kind is 'scatter':
    #    for i,yi in enumerate(y):
    #        if i is 0:
    #            df.plot(x=x,y=yi,rot=25,kind=kind,ax=ax,color=colors[i],label=yi)
    #        else:
    #            df.plot(x=x,y=yi,rot=25,kind=kind,ax=ax,color=colors[i],label=yi)
    #    ax.set_xlabel(x[0],fontsize=24)  
    #    definePlotLabels(ax,y,kind)
    #elif kind is 'area':
    #    
    #    if ( x is not None ):
    #        print 'plot not generated: area plot only supports time series plotting'
    #        return
    #    if ( y is None ):
    #        df.plot(rot=25,ax=ax,kind=kind,stacked=stacked)
    #    else:
    #        df.plot(y=y,rot=25,kind=kind,stacked=stacked)
    #        definePlotLabels(ax,y,kind)
    #        
    #    
    #elif kind is 'hexbin':
    #    
    #    if ( len(y) > 1 ):
    #        print 'Only one y value can be plotted with hexbin'
    #        return
    #    
    #    df.plot(x=x,y=y,rot=25,ax=ax,kind=kind,gridsize=gridsize)
    #    ax.set_xlabel(x[0],fontsize=24)  
    #    definePlotLabels(ax,y,kind)
    #        
    #elif kind is 'pie':
    #    print 'pie plots currently not supported'
    #    return
    #elif kind is 'line' or kind is None:
    #    if ( x is not None ):
    #        print 'plot not generated: area plot only supports time series plotting'
    #        return
    #    if ( y is None ):
    #        df.plot(rot=25,ax=ax,kind=kind)
    #    else:
    #        df.plot(y=y,rot=25,kind=kind)
    #        definePlotLabels(ax,y,kind)
    #
    #else:
    #    print 'unknown plot kind'
    #    return
    #
    #fig.show()