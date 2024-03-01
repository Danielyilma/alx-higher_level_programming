#!/usr/bin/python3
'''using http response as json'''
import requests
import sys


def main():
    url = sys.argv[1]
    posted_data = {'q': ""}
    if len(sys.argv) > 2 and sys.argv[2]:
        posted_data['q'] = sys.argv[2]

    r = requests.post(url, data=posted_data)

    try:
        json = r.json()
        print(json.get('message'))
        if len(json) == 0:
            print('No result')
        else:
            print(f'[{json.get('id')}] {json.get('name')}')
    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')

if __name__ == '__main__':
    main()
