#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    max_value = float('-inf')
    best_key = None

    for key, item in a_dictionary.items():
        if item > max_value:
            max_value = item
            best_key = key

    return (best_key)
