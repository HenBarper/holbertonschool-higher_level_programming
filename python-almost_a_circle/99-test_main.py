#!/usr/bin/python3
""" test main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 1, 1, 99)
    r1.save_to_file([])
