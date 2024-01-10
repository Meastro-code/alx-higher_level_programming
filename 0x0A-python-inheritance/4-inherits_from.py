#!/usr/bin/python3
"""
   function that returns true if subcalss
"""
def inherits_from(obj, a_class):
    """ function that returns true if subclass """
    return issubclass(type(obj), a_class)
