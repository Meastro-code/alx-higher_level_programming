#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{:d} argument{}.".format(argc, "" if argc == 1 else "s"))
    else:
        print("{:d} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
