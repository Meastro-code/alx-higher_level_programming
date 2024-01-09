#!/usr/bin/python3
def write_file(filename="", text=""):
    """ function to write a file """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
