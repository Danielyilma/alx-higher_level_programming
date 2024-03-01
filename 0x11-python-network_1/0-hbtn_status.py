#!/usr/bin/python3
'''fetching data from a url'''
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()
    print('''Body response:\n\t- type: {}\n\t- \
content: {}\n\t- utf-8 content: {}'''.format(
        type(data), data, data.decode("utf-8")
    ))
