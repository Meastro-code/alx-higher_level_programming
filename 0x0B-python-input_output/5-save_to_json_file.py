#!/usr/bin/python3
"""
   Writes an object to a text file
"""
import json

def save_to_json_file(my_obj, filename):
    """ function to write an object to a file """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
