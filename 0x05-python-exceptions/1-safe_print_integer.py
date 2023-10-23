#!/usr/bin/python3
def safe_print_integer(value):
    int_val = 0
    try:
        if int_val == int(value):
            return True
    except ValueError:
        return False
