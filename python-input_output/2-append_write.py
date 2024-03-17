#!/usr/bin/python3
"""Function that appends element to end of list"""

def append_write(filename = "", text = ""):
    """appends string to end of utf-8 text file"""
    with open(filename, "a", encoding="utf-8") as the_file:
        return the_file.write(text)