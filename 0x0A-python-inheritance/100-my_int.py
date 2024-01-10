#!/usr/bin/python3
"""
   MyInt class inheritance int
"""
class MyInt(int):
    """ function that checks for equality """
    def __eq__(self, other):
        return int(self) != other
    """ function that returns other object """
    def __ne__(self, other):
        return int(self) == other
