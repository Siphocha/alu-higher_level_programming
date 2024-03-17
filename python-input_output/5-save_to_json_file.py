#!/usr/bin/python3
"""writes object to text file using  JSON"""
import json

def save_to_json_file(my_obj, filename):
    """riting object to text file using JSON"""
    with open(filename, "w", encoding="utf-8") as n:
        json.dump(my_obj, n)
