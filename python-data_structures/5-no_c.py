#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for theChar in my_string:
        if(theChar not in "cC"):
            new_string += theChar
    return new_string
