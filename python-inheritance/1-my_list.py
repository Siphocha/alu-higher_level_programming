#!/usr/bin/python3
"""An empty list with empty test function for defining lists"""
class MyList(list):
    def print_sorted(self):
        """defining function for printing sorted list"""
        print(sorted(self))
