#!/usr/bin/python3
"""
   a script that adds all arguments to a Python list,
   and then save them to a file
"""
import sys
import json
from os import path

def save_to_json_file(my_obj, filename):
    """ function to save to a file """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """ function to read from a file """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    filename = 'add_item.json'
    if not path.exists(filename):
        save_to_json_file([], filename)
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
