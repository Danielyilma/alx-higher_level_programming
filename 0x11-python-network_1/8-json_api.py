#!/usr/bin/python3
'''using http response as json'''
import requests
import sys


def main():
    url = 'http://0.0.0.0:5000/search_user'
    posted_data = {'q': ""}
    if len(sys.argv) > 1 and sys.argv[1]:
        posted_data['q'] = sys.argv[1]

    r = requests.post(url, data=posted_data)

    try:
        json = r.json()
        if len(json) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')


if __name__ == '__main__':
    main()
