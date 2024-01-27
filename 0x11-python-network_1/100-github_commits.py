#!/usr/bin/python3
'''A script that takes 2 arguments in order to solve this challenge
'''
import requests
import sys


if __name__ == '__main__':
    repo_n = sys.argv[2]
    owner_n = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo_n, owner_n)

    r = requests.get(url)

    com = r.json()
    try:
        for i in range(10):
            sha = com[i].get('sha')
            auth_n = com[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, auth_n))
    except IndexError:
        pass
