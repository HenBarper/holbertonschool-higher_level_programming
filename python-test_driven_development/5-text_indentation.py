#!/usr/bin/python3
""" 4. Text indentation - 5-text_indentation.py """


def text_indentation(text):
    """
    This function prints a text w/ 2 new lines\
        after each: '.' '?' or ':'

    Args:
        text: text to use

    Raises:
        TypeError if text not a string

    Return:
        No return only print
    """
    for char in text:
        print(char, end='')
        if char in ['.', '?', ':']:
            print()
            print()
