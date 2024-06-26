#!/usr/bin/python3
"""Function for saying your name outloud called say_my_name"""

def say_my_name(first_name, last_name=" "):
    """functionfor printing first-and-last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    """printing both the names being printed out"""
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
