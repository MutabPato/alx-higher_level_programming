#!/usr/bin/python3
def no_c(my_string):
    result = []
    for a in my_string:
        if a == 'c' or a == 'C':
            continue
        else:
            result.append(a)
    return (''.join(result))
