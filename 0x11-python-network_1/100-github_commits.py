#!/usr/bin/python3
import requests
import sys


def main():
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]
    )
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print('{}: {}'.format(
            commits[i].get('commit').get('tree').get('sha'),
            commits[i].get('commit').get('author').get('name')
        ))


if __name__ == '__main__':
    main()
