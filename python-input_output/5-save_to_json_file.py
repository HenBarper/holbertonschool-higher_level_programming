#!/usr/bin/python3
"""
Write a function that writes an Object to
    a text file, using a JSON representation:

Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes an obj to a text file in json representation"""
    with open(filename, 'w', encoding='utf-8') as writefile:
        writefile.write(json.dumps(my_obj))
