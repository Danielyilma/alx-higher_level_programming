#!/usr/bin/python3
'''handing http responses'''
import urllib
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data.decode('utf-8'))

except urllib.error.URLError as e:
    print('Error code: {}'.format(e.code))
