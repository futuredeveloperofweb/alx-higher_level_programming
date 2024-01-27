#!/usr/bin/python3
'''A script that takes 2 arguments in order to solve this challenge
'''
import requests
import requests.auth
import sys


if __name__ == '__main__':
    repo_n = sys.argv[1]
    owner_n = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo_n, owner_n)

    r = requests.get(url)

    try:
        commits = r.json()
        for com in commits[:10]:
            sha = com['sha']
            auth_n = com['commit']['author']['name']
            print('{}: {}'.format(sha, auth_n))
    except ValueError:
        print('None')
