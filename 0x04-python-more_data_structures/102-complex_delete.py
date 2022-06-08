#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    arr = []
    for n in a_dictionary:
        if a_dictionary[n] == value:
            arr.append(n)
        else:
            continue
    for x in arr:
        del a_dictionary[x]
    return a_dictionary
