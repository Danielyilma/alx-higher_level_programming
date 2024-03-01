#!/usr/bin/python3
'''fetching data from a url'''
from urllib import request


def main():
    '''This Python script is fetching datausing the
     `urlopen` function from the `urllib.request` module.'''
    url = "https://alx-intranet.hbtn.io/status"
    req = request.Request(url)
    with request.urlopen(req) as response:
        data = response.read()
        print('''Body response:\n    - type: {}\n    - \
content: {}\n    - utf-8 content: {}'''.format(
            type(data), data, data.decode("utf-8")
        ))


if __name__ == '__main__':
    main()
