#!/usr/bin/python3
"""Function that returns number of lines in file"""

def write_file(filename = "", text=""):
    """writes string file (UTF-8) and counts all lines"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)