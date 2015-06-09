from fitbittools.fbdata import FitBitData
from fitbittools.plotters import Plotter

filename="/Users/frenchwr/Computing/Python/Fitbit/data/fitbit_export_20140710.csv"
fb_obj = FitBitData(filename)
activity = fb_obj.activity.pd_data
sleep = fb_obj.sleep.pd_data
plotter = Plotter()
plotter.plot_data_frame(activity,kind='bar',stacked=True)
plotter.plot_data_frame(activity) # default kind is line
plotter.plot_data_frame(sleep,kind='bar',stacked=True)
plotter.plot_data_frame(activity,kind='area')
plotter.plot_data_frame(activity,x='Minutes Sedentary',
                        y='Minutes Very Active',kind='hexbin')
plotter.plot_data_frame(sleep,kind='hist',stacked=True)
plotter.plot_data_frame(activity,kind='box')
plotter.plot_data_frame(activity,y=['Minutes Very Active',
                        'Minutes Lightly Active'],kind='pie')
plotter.plot_data_frame(sleep,x='Minutes Asleep',
                        y='Minutes Awake',kind='scatter')