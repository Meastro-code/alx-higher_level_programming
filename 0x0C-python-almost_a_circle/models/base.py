#!/usr/bin/python3
"""
  Class Base
"""
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ function init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
