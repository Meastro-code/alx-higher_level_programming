#!/usr/bin/python3
"""
   Class student to create object student
"""
class Student:
    def __init__(self, first_name, last_name, age):
        """ function to create object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function to convert to json """
        return self.__dict__
