#!/usr/bin/python3
# This script replaces an element in the list with another.

def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list