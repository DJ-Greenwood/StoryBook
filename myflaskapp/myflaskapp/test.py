import os
import json
import sqlite3

def read_json_files(json_file_directory):
    """
    Read all JSON files in the specified directory.
    
    :param json_file_directory: Path to the directory containing JSON files.
    :return: A list of data from all JSON files.
    """
    data_list = []
    for name in os.listdir(json_file_directory):
        if name.endswith('.json'):
            data_list.append(name)
    return data_list

print(read_json_files('myflaskapp/Include/NewJson/'))