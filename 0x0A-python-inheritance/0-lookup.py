#!/usr/bin/python3
"""
   Function lookup
"""
def lookup(obj):
    """ function that returns lists of attributes and methods of obj """
    return [attr for attr in dir(obj)]
