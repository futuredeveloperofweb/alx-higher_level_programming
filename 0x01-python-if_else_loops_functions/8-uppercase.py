#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for s in str:
        if 'a' <= s <= 'z':
            char = chr(ord(s) - 32)
            upper += char
        else:
            upper += s
    print('{}'.format(upper))
