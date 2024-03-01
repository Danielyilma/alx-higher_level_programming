#!/usr/bin/python3
'''getting the value of the HTTP responce header'''
from urllib import request
import sys

def main():
    """
    The `main` function takes a URL as a command line argument
    the value of the "X-Request-Id" header from the response.
    """
    url = sys.argv[1]

    with request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == '__main__':
    main()