#!/usr/bin/python3
'''post request'''
import requests
import sys


def main():
    url = sys.argv[1]
    post_data = {'email': sys.argv[2]}
    r = requests.post(url, data=post_data)
    print(r.content.decode('utf-8'))


if __name__ == '__main__':
    main()
