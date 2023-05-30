#!/usr/bin/python3
"""
Write a function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:

Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean
You are not allowed to import any module
"""


def class_to_json(obj):
    """Function to return dict description of class"""
    dict_desc = {}

    attributes = obj.__dict__

    for attr, value in attributes.items():
        if type(value) in [list, dict, str, int, bool]:
            dict_desc[attr] = value
    return dict_desc
