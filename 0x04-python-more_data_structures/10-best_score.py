#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxk = None
    maxv = 0
    for k, v in a_dictionary.items():
        if maxv < v:
            maxk = k
            maxv = v
    return maxk
