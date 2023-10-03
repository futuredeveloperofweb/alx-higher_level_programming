#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for s in str:
        if 'a' <= s <= 'z':
            s += chr(ord(s) - 32)
            upper += s
        else:
            upper += s
    print('{}'.format(str))
