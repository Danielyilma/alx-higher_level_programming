#!/usr/bin/python3
'''getting the value of the HTTP responce header'''
import urllib.request
import sys


def main():
    """
    The `main` function takes a URL as a command line argument
    the value of the "X-Request-Id" header from the response.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == '__main__':
    main()
