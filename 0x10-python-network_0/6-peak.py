#!/usr/bin/python3
'''function that finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):

    size = len(list_of_integers)
    m = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        m = m // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if m // 2 == 0:
                m = 2
            mid = mid + m // 2
        elif m > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if m // 2 == 0:
                m = 2
            mid = mid - m // 2
        else:
            return list_of_integers[mid]
