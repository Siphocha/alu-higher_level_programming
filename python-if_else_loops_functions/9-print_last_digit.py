#!/usr/bin/python3
def present_last_digit(num):
    if num < 0:
        num = -num
        #last digit is the number divided by 10
    present_last_digit = num % 10
    print("{}".format(present_last_digit), end="")
    return present_last_digit