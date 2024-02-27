#!/usr/bin/python3
#This program prints all ASCI characters except two all in lowercase.
for i in range(97, 123):
    if chr(i) not in ["q", "e"]:
        print("{}".format(chr(i)), end="")