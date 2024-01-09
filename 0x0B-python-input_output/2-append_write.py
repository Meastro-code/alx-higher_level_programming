#!/usr/bin/python3
"""
   function to create and append on file
"""
def append_write(filename="", text=""):
    """ fucntion to append or create """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
