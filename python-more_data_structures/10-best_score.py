#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    highscore = list(a_dictionary.values())[0]
    theKey = None
    for key, value in a_dictionary.items():
        if value > highscore:
            highscore = value
            theKey = key
    return theKey
