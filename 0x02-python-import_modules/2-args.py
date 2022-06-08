#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv)
    if args <= 1:
        print("0 arguments.")
    else:
        if args == 2:
            print("{:d} argument:".format(args - 1))
        else:
            print("{:d} arguments:".format(args - 1))
        for i in range(1, args):
            print("{:d}: {}".format(i, sys.argv[i]))
