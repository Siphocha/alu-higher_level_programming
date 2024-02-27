#!/usr/bin/python3
#script that prints combination of two numbers in ascending order.
for f_num in range (0, 10):
    #second number loop is subsidiary of one because it comes after.
    for s_num in range(f_num + 1, 10):
        #number specific to output type preferred
        if f_num == 8 and s_num == 9:
            print("{:02d}".format(f_num * 10 +  s_num))
        else:
            print("{:02d}, ".format(f_num * 10 + s_num), end="")

