#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    lengthh = len(argv)
    sum = 0
    for i in range(1, lengthh):
        sum += int(argv[i])
    print("{:d}".format(sum))
