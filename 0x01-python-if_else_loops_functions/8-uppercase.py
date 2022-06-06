#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

def uppercase(str):
    for c in str:
        value = ord(c) - 32 if islower(c) else ord(c)
        print("{:c}".format(value), end="")
    print()
