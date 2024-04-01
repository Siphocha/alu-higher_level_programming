#!/usr/bin/python3
"""making a function for adding integers
Call that add_integer"""
import doctest

def add_integer(a, b=98):
    """This is the function for adding"""
    if type(a) not in(int, float):
        raise TypeError("a must be an integer")
    if type(b) not in(int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    doctest.testfile("tests/0-add_integer.txt")
    