#!/usr/bin/python3
""" test main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    json_dictionary = Base.to_json_string()
