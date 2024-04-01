#!/usr/bin/python3
"""Function for printing suqare with #"""

def print_square(size):
    """Function for printing #-square shape"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    """printing square with hashtags"""
    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")