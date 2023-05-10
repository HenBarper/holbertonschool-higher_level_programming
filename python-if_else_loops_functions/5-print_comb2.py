#!/usr/bin/python3
for i in range(100):
    if(i < 99):
        print("{00}, ".format(i), end = '')
    else:
        print("{00}".format(i))
