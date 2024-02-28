#!/usr/bin/python3
# This script has a function that finds all multiples of 2.


def divisible_by_2(my_list=[]):
    multiples = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)