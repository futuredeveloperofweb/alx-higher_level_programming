#!/usr/bin/python3
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        print(resp.headers.get("X-Request-Id"))
