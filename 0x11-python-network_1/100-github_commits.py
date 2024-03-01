#!/usr/bin/python3
'''getting a commit from github api'''
import requests
import sys


def main():
    '''main function'''
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]
    )
    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')
            ))
    except Exception as e:
        pass

if __name__ == '__main__':
    main()
