#!/usr/bin/python3
"""
This module describes a function to find the peak
in a list of values
"""


def find_peak(list_of_integers):
    """
    Function to find the peak
    """

    if (list_of_integers == []):
        return (None)

    i = 0
    for elem in list_of_integers:
        elem = list_of_integers[i]
#        if (elem == list_of_integers[0]):
        if i == 0:
            continue
#        else if (elem == list_of_integers[(len(list_of_integers) - 1)]):
        elif (i == len(list_of_integers) - 1):
            return(None)
        else:
            if (list_of_integers[i - 1] <= elem and elem >= list_of_integers[i + 1]):
                return(elem)
            else:
                i = i + 1
                continue
