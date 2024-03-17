#!/usr/bin/python3
"""returns simple dictionary data dtstructure (list. dictionary, string, integer & boolean)"""

def class_to_json(obj):
    """Return dictionary description of object"""
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res