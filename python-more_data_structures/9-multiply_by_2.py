#!/usr/bin/python3
# This script has a function that returns a dictionary with all key values bultiplied by 2. (surface level encryption??)
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for n in list_keys:
        new_dir[n] *= 2
    return (new_dir)