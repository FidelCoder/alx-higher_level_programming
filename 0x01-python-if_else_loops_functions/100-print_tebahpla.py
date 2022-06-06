#!/usr/bin/python3
for i in range(122, 96, -1):
    copy = i
    if (copy % 2 != 0):
        copy -= 32
    print("{}".format(chr(copy)), end="")
