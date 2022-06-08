#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for n in sorted(a_dictionary):
        print("{}: {}".format(n, a_dictionary[n]))
