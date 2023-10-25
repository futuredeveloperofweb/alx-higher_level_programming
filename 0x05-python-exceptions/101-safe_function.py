#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        v = fct(*args)
        return v
    except Exception as err:
        print('Exception: {}'.format(err), file=sys.stderr)
        return None
