#!/usr/bin/python3def
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
