#!/usr/bin/python3
for f_num in range (0, 10):
    for s_num in range(f_num + 1, 10):
        if f_num == 8 and s_num == 9:
            print("{:02d}".format(f_num * 10 +  s_num))
        else:
            print("{:02d}, ".format(f_num * 10 + s_num), end="")

