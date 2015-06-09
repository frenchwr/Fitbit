import re # regex package
import pandas as pd
import fitbittools.cleaners as cln

class DataBase:
    """Abstract class for data categories"""
    def __init__(self,filename,start_line,data_size,clean=True):
        self.pd_data = pd.read_csv(filename,skiprows=start_line,
                                   nrows=data_size,index_col=0)
        if clean: 
            cleaner = cln.Cleaner()
            cleaner.remove_commas(self.pd_data)
            self.pd_data = cleaner.zap_zeros(self.pd_data)

class Activity(DataBase):
    """Stores activity data"""
    def __init__(self,filename,start_line,data_size,clean=True):
        # pandas data frame
        self.pd_data = None
        # numpy arrays
        self.calories = None
        self.steps = None
        self.distance = None
        self.floors = None
        self.sedentary = None
        self.lightly_active = None
        self.fairly_active = None
        self.very_active = None
        self.activity_calories = None
        if start_line is not None:
            DataBase.__init__(self,filename,start_line,data_size,clean)
            self.calories = self.pd_data['Calories Burned'].values
            self.steps = self.pd_data['Steps'].values
            self.distance = self.pd_data['Distance'].values
            self.floors = self.pd_data['Floors'].values
            self.sedentary = self.pd_data['Minutes Sedentary'].values
            self.lightly_active = self.pd_data['Minutes Lightly Active'].values
            self.fairly_active = self.pd_data['Minutes Fairly Active'].values
            self.very_active = self.pd_data['Minutes Very Active'].values
            self.activity_calories = self.pd_data['Activity Calories'].values

class Sleep(DataBase):
    """Stores sleep data"""
    def __init__(self,filename,start_line,data_size,clean=True):
        # pandas data frame
        self.pd_data = None
        # numpy arrays
        self.asleep = None
        self.awake = None
        self.num_awakenings = None
        self.in_bed = None
        if start_line is not None:
            DataBase.__init__(self,filename,start_line,data_size,clean)
            self.asleep = self.pd_data['Minutes Asleep'].values
            self.awake = self.pd_data['Minutes Awake'].values
            self.num_awakenings = self.pd_data['Number of Awakenings'].values
            self.in_bed = self.pd_data['Time in Bed'].values

class Weight(DataBase):
    """Stores weight data"""
    def __init__(self,filename,start_line,data_size,clean=True):
        # pandas data frame
        self.pd_data = None
        # numpy arrays
        if start_line is not None:
            DataCategory.__init__(self,filename,start_line,data_size,clean)

class FitBitData:
    """Fitbit data container"""
    def __init__(self,filename,clean=True):
        start_lines,data_size = self.get_file_info(filename)
        self.activity = Activity(filename,start_lines[0],data_size[0],clean)
        self.sleep = Sleep(filename,start_lines[1],data_size[1],clean)
        self.weight = Weight(filename,start_lines[2],data_size[2],clean)

    def get_file_info(self,filename):
        """finds initial line and total lines for each category"""
        line_numbers = [None,None,None]
        in_category_section = [False,False,False]
        data_size = [0,0,0]
        with open(filename) as f:
            for line, text in enumerate(f):
                if re.match("(A|a)ctivit",text):
                    line_numbers[0] = line + 1
                    in_category_section[0] = True
                elif re.match("(S|s)leep",text):
                    line_numbers[1] = line + 1
                    in_category_section[1] = True
                elif re.match("(W|w)eight",text):
                    line_numbers[2] = line + 1
                    in_category_section[2] = True
                elif text in ['\n', '\r\n']:
                    in_category_section = [False,False,False]
                for i,in_section in enumerate(in_category_section):
                    if in_section and line >= line_numbers[i]+1: 
                        data_size[i] += 1
        return line_numbers,data_size  
