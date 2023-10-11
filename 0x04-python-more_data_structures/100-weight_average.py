#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    s = 0
    d = 0
    for t in range(len(my_list)):
        s += my_list[t][0] * my_list[t][1]
        d += my_list[t][1]
    return s/d
