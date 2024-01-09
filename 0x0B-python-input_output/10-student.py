#!/usr/bin/python3
"""
   class Student that defines a student by:
   (based on 9-student.py)
"""
class Student:
    def __init__(self, first_name, last_name, age):
        """ function to create the student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function to convert to json """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
