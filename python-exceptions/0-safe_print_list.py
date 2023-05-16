#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        i -= 1
        try:
            if(i < x):
                print("{}".format(my_list[i]), end='')
                count += 1
        except ValueError:
            pass
    print()
    return count
