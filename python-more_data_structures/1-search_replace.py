#!/usr/bin/python3
# This function replaces a character in a list by making a new list without that character
def search_replace(my_list, search, replace):
    new_list = list(map(lambda n: replace if n == search else n, my_list))
    return (new_list)