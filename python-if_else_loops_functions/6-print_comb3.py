#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if(i != j):
            print("{0:d}{1:d}".format(i, j), end='')
            if(i == 8 and j == 9):
                print()
            else:
                print(", ", end='')
