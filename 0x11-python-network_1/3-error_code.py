#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and
displays the body of the response'''
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    data = urllib.parse.urlencode([])
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
