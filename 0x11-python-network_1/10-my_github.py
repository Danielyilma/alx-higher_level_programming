#!/usr/bin/python3
'''gettin user data from github api'''
import requests
import sys


def main():
    '''main method'''
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwd = sys.argv[2]
    credential = {
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f'Bearer {passwd}',
        'Accept': 'application/vnd.github+json'
    }
    r = requests.get(url, headers=credential)
    print(r.json().get('id'))


if __name__ == '__main__':
    main()