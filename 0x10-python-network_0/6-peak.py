#!/usr/bin/python3
'''a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''
    Args:
        list_of_integers(int): list of integers
    Returns: the peak of the list or None
    '''
    size = len(list_of_integers)
    mid_e = size
    m = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (m < size - 1 and
                list_of_integers[m] < list_of_integers[m + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            m = m + mid_e // 2
        elif mid_e > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            m = m - mid_e // 2
        else:
            return list_of_integers[m]
