#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_1 = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return tuple_1
