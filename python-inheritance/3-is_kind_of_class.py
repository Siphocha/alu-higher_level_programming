#!/usr/bin/python3
"""Function for object checking"""

def is_kind_of_class(obj, a_class):
    """checks if object is its own or child of parent class"""
    if isinstance(obj, a_class):
        return True
    return False