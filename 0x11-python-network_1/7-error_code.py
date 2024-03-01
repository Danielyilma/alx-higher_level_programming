#!/usr/bin/python3
'''printing error code if there is one'''
import requests
import sys


def main():
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.content.decode('utf-8'))

if __name__ == '__main__':
    main()
