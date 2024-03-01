#!/usr/bin/python3
'''post an email adderess to the given url'''
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
param = {
    'email': sys.argv[2]
}

data = urllib.parse.urlencode(param).encode('ascii')
url = urllib.request.Request(url, data)

with urllib.request.urlopen(url) as response:
    print(response.read().decode('utf-8'))
