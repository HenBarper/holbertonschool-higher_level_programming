#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
str1 =  "and is greater than 5"
str2 = "and is zero"
str3 = "and is less than 6 but not 0"
if(last_dig > 5):
    str4 = str1
elif(last_dig == 0):
    str4 = str2
else:
    str4 = str3
print(f"Last digit of {number} is {last_dig} {str4}")
