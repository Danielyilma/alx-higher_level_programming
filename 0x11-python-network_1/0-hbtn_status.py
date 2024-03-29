#!/usr/bin/python3
'''fetching data from a url'''
import urllib.request


def main():
    '''This Python script is fetching datausing the
     `urlopen` function from the `urllib.request` module.'''
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'''.format(
            data.decode("utf-8")
        ))


if __name__ == '__main__':
    main()
