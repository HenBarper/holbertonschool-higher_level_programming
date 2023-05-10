#!/usr/bin/python3
def uppercase(str):
    strLength = len(str)
    for i in range(strLength):
        if(ord(str[i]) >= 97 and ord(str[i]) <= 122):
            str[i] = (ord(str[i]) -= 32)
