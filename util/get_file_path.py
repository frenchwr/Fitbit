import os
import inspect

def get_file_path(input_file):
    script_name = inspect.getframeinfo(inspect.currentframe()).filename
    script_path = os.path.dirname(os.path.abspath(script_name))
    data_file = script_path + "/../data/" + input_file
    return data_file