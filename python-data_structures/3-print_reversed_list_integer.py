#!/usr/bin/python3
# This function prints integers of a list but in reverse order!


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for n in my_list:
            print("{:d}".format(n))