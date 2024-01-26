#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type:', type(r))
print('\t- content:', r)
