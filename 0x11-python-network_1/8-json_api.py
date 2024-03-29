#!/usr/bin/python3
'''script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter'''
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]
    let = {'q': q}
    r = requests.post(url, data=let)

    try:
        resp = r.json()
        if resp == {}:
            print('No result')
        else:
            print('[{}] {}'.format(resp.get('id'), resp.get('name')))
    except ValueError:
        print('Not a valid JSON')
