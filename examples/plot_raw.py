from util.get_file_path import get_file_path
from util.read_raw_CSV import read_raw_CSV
from util.wrappers import plot_data_frame

data_file = get_file_path("fitbit_export_20140710.csv")
[activity,sleep] = read_raw_CSV(data_file,["Activity","Sleep"])
#allData = pd.concat([activity,sleep])

# 11/02/2014
# I spent a lot of time previously optimizing the layout of the axis and tick labels
# but when I updated all my python pacakges several months later everything was 
# broken...I'm just going to keep these plotting wrappers very minimal from now
# on and update the aestetics if I really need to

plot_data_frame(activity) # default kind is line
plot_data_frame(sleep,kind='bar',stacked=True)
plot_data_frame(activity,kind='area')
plot_data_frame(activity,x='Minutes Sedentary',y='Minutes Very Active',kind='hexbin')
plot_data_frame(sleep,kind='hist',stacked=True)
plot_data_frame(activity,kind='box')
plot_data_frame(activity,y=['Minutes Very Active','Minutes Lightly Active'],kind='pie')
plot_data_frame(sleep,x='Minutes Asleep',y='Minutes Awake',kind='scatter')