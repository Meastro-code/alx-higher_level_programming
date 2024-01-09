#!/usr/bin/python3
"""
   class Student that defines a student by:
   (based on 10-student.py)
"""
class Student:
    def __init__(self, first_name, last_name, age):
        """ function to create student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a function to convert to json """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ a function to load from json """
        for key, value in json.items():
            setattr(self, key, value)
