#!/usr/bin/python3
"""
   function to read a file
"""
def read_file(filename=""):
    """ function to read a text file """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
