import re # regex package
import pandas as pd
import fitbittools.cleaners as cln

class DataBase:
    """Abstract class for data categories"""
    def __init__(self,filename,start_line,data_size):
        self.pd_data = pd.read_csv(filename,skiprows=start_line,
                                   nrows=data_size,index_col=0)

class Activity(DataBase):
    """Stores activity data"""
    def __init__(self,filename,start_line,data_size):
        # pandas data frame
        self.pd_data = None
        if start_line is not None:
            DataBase.__init__(self,filename,start_line,data_size)

class Sleep(DataBase):
    """Stores sleep data"""
    def __init__(self,filename,start_line,data_size):
        # pandas data frame
        self.pd_data = None
        if start_line is not None:
            DataBase.__init__(self,filename,start_line,data_size)

class Weight(DataBase):
    """Stores weight data"""
    def __init__(self,filename,start_line,data_size):
        # pandas data frame
        self.pd_data = None
        if start_line is not None:
            DataBase.__init__(self,filename,start_line,data_size)

class FitBitData:
    """Fitbit data container"""
    def __init__(self,filename,clean=True):
        start_lines,data_size = self.get_file_info(filename)
        self.activity = Activity(filename,start_lines[0],data_size[0])
        self.sleep = Sleep(filename,start_lines[1],data_size[1])
        self.weight = Weight(filename,start_lines[2],data_size[2])
        self.comp_pd_data = pd.concat([self.sleep.pd_data, self.activity.pd_data], axis=1)
        if clean: 
            cleaner = cln.Cleaner()
            self.activity.pd_data = cleaner.clean_dataframe(self.activity.pd_data)
            self.sleep.pd_data = cleaner.clean_dataframe(self.sleep.pd_data)
            self.comp_pd_data = cleaner.clean_dataframe(self.comp_pd_data)

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
