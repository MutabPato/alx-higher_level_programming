#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i, a in enumerate(str):
        if n != i:
            result += a
    return result
