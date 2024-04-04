#!/usr/bin/python3
"""Function returns object represented as JSON string"""
import json

def to_json_string(the_obj):
    """returns json string"""
    return json.dumps(the_obj)