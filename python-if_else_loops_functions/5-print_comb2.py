#!/usr/bin/python3
#This script prints upto 99 with spaces in-between.
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num))