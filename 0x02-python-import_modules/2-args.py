#!/usr/bin/python3
from sys import argv


def main():
    print("{} arguments{}".format(len(argv) - 1, "."
                                  if len(argv) == 1 else ":"))
    for i, string in enumerate(argv[1:]):
        print("{0}: {1}".format(i + 1, string))


if __name__ == "__main__":
    main()
