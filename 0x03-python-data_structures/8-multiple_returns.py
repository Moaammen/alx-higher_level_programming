#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        tuple_1 = (len(sentence), sentence[0])
        return tuple_1
