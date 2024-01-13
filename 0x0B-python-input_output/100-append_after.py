#!/usr/bin/python3
"""task 13"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        line_l = []
        while True:
            line = file.readline()
            if line == '':
                break
            line_l.append(line)
            if search_string in line:
                line_l.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_l)
