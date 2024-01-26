#!/usr/bin/python3
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        x_request_id = resp.getheader('X-Request-Id')
        print(x_request_id)
