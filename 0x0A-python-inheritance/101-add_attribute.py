#!/usr/bin/python3
"""
   Function to add attribute
"""
def add_attribute(obj, name, value):
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
