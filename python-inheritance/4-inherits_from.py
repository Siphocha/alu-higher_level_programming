#!/usr/bin/python3
"""Plain function for chekcing object class-status"""

def inherits_from(obj, a_class):
    """Checks if object is in child-class inherited from parent class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False