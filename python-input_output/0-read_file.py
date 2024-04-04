#!/usr/bin/python3
"""Function for reading simple-file"""

def read_file(filename=""):
    """reading file instructions"""
    with open(filename, "r", encoding="utf-8") as n:
        text = n.read()
        print(text, end="")