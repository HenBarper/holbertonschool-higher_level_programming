#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = 0

    if(number > 0):
        lastDigit = number % 10
    elif(number < 0):
        lastDigit = number % -10
    else:
        pass
    
    print(lastDigit)
    return lastDigit
