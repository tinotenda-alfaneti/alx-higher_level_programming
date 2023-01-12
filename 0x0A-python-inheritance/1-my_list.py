#!/usr/bin/python3
# 1-my_list.py
"""Defines a derived class name MyList"""


class MyList(list):
    """implement print_sorted method"""

    def print_sorted(self):
        """sort in ascending order"""
        list_copy = self[::]
        list_copy.sort()
        print(list_copy)
