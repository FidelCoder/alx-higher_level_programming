#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        dic_add = {key: value}
        a_dictionary.update(dic_add)
    else:
        a_dictionary[key] = value
    return a_dictionary
