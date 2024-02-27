#!/usr/bin/python3
#This script checks for lower case characters.
def islower(c):
    #scans the ASCII characters for the lowercase ones
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False