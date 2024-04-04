#!/usr/bin/python3
"""Below we are defining function for class verification"""

def is_same_class(obj, a_class):
    """check if object is really part of class"""
    if type(obj) == a_class:
        return True
    return False