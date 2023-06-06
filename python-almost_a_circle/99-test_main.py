#!/usr/bin/python3
""" test main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3)
    Rectangle.save_to_file(r1.to_dictionary())
