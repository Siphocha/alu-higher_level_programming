#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:  # Check if the sentence is not empty
        return len(sentence), sentence[0]
    else:
        return 0, None