#!/usr/bin/python3
"""creating object from JSON file"""
import json

def load_from_json_file(filename):
    """creating object from JSON file"""
    with open(filename, "r", encoding="utf-8") as n:
        return json.load(n)