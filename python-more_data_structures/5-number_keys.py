#!/usr/bin/python3
# Script that runs a function that returns num of keys in dictionary.
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return (num)