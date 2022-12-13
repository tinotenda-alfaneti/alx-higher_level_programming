#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    max_ = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_:
            max_ = my_list[i]

    return (max_)
