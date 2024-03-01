#!/usr/bin/python3
'''getting the value of the HTTP responce header'''
import urllib
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
