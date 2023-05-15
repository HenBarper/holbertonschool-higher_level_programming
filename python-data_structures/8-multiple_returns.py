#!/usr/bin/python3


def multiple_returns(sentence):
    if(sentence == ""):
        nuple = (len(sentence), None)
    else:
        nuple = (len(sentence), sentence[0])
    return nuple
