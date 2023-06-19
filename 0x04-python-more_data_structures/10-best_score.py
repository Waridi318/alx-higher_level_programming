#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return(None)
    d = 0
    key = None
    for i, v in a_dictionary.items():
        if v > d:
            d = v
            key = i
    return(key)
