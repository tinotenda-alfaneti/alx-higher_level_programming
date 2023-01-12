#!/usr/bin/python3
# 1-my_list.py
"""Defines a derived class name MyList"""

class MyList(list):
    """implement print_sorted method"""

    def print_sorted(self):
        """sort in ascending order"""
        cpy = self[:]
        cpy.sort()
        return cpy
