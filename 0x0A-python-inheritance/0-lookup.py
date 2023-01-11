#!/usr/bin/python3
# 0-lookup.py
"""Defines an object methods and attributes lookup function."""


def lookup(obj):
    """Return a list of object's methods and attributes."""
    return (dir(obj))
