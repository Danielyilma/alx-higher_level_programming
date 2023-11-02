#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for i, numstring in enumerate(argv[1:]):
        sum += int(numstring)
    print("{}".format(sum))


if __name__ == "__main__":
    main()
