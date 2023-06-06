#!/usr/bin/python3
""" test main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(2, 1, 1, 99)
    print(s1.to_dictionary())
