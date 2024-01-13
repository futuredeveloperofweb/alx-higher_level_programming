#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ''
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            my_new_string += my_string[i]
    return my_new_string
