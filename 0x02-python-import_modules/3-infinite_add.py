#!/usr/bin/python3
import sys
length = len(sys.argv)
result = 0
if __name__ == "__main__":
    if length == 1:
        result = 0
    else:
        for i in range(1, length):
            result += int(sys.argv[i])
    print("{:d}".format(result))
