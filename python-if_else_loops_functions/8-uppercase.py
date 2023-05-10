#!/usr/bin/python3
def uppercase(str):
    ascNum = 0
    strLength = len(str)
    for i in range(strLength):
        ascNum = ord(str[i])
        if(ascNum >= 97 and ascNum <= 122):
            ascNum -= 32
        print(f"{chr(ascNum)}".format(), end='')
    print()
