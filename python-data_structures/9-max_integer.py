#!/usr/bin/python3


def max_integer(my_list=[]):
    if((len(my_list)) == 0):
        return None
    else:
        bigNum = 0
        for i in my_list:
            if(i > bigNum):
                bigNum = i
        return bigNum
