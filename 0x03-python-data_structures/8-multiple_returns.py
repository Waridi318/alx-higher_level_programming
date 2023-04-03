#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)

    if i == 0:
        return(i, None)
    return(i, sentence[0])
