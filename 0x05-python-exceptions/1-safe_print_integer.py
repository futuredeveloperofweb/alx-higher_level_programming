#!/usr/bin/python3
def safe_print_integer(value):
    int_val = 0
    try:
        int_val == int(value)
        print('{:d}'.format(value))
        return True
    except ValueError:
        return False
