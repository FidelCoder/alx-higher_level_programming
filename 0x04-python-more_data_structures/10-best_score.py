#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) < 1:
        return None
    first = True
    x = 0
    s = ''
    for n in a_dictionary:
        if first:
            x = a_dictionary[n]
            s = n
            first = False
        elif x < a_dictionary[n]:
            s = n
            x = a_dictionary[n]
        else:
            continue
    return s
