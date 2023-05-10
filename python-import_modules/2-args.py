#!/usr/bin/python3
import sys

if __name__ == "__main__":
    theString = "{:d} argument"
    vLen = len(sys.argv) - 1
    if vLen == 0:
        theString += 's.'
    elif vLen == 1:
        theString += ':'
    else:
        theString += 's:'
    print(theString.format(vLen))

    i = 0
    for argument in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, argument))
        i += 1
