#!/usr/bin/python3
'''handing http responses'''
from urllib import request, error
import sys


def main():
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))

    except error.URLError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    main()
