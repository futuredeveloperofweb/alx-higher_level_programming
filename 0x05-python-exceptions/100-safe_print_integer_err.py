#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    i = True
    try:
        print('{:d}'.format(value))
    except Exception as err:
        print('Exception:', err, file=sys.stderr)
        i = False
    return i
