#!/usr/bin/python3
"""function returns object rep in JSOn string"""
import json

def from_json_string(my_str):
    """Return object by JSON"""
    return json.loads(my_str)
