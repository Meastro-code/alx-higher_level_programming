#!/usr/bin/python3
"""
   Class MyList
"""
class MyList(list):
    def print_sorted(self):
        """ fucntion to sort list """
        sorted_list = sorted(self)
        print(sorted_list)
