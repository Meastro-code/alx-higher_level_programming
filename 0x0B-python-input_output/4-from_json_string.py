#!/usr/bin/python3
"""
   Function that returns an object
"""
import json

def from_json_string(my_str):
    """ a function that returns an object """
    return json.loads(my_str)
