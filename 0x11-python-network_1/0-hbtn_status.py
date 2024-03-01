#!/usr/bin/python3
'''fetching data from a url'''
from urllib import request


def main():
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        data = response.read()
        print('''Body response:\n\t- type: {}\n\t- \
    content: {}\n\t- utf-8 content: {}'''.format(
            type(data), data, data.decode("utf-8")
        ))


if __name__ == '__main__':
    main()
