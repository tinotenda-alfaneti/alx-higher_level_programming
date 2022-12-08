#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ky = list(a_dictionary.keys())[0]
    max_so_far = a_dictionary[ky]
    for k, v in a_dictionary.items():
        if v > max_so_far:
            max_so_far = v
            ky = k
    return (ky)
