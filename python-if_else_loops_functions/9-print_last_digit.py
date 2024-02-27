#!/usr/bin/python3
def present_last_digit(num):
    if num < 0:
        num = -num
    present_last_digit = num % 10
    print("{}".format(present_last_digit), end="")
    return present_last_digit