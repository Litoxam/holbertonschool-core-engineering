#!/usr/bin/env python3


def best_score(a_dictionary):
    """returns the key with the biggest integer value"""
    if not a_dictionary:
        return None
    best_score = max(a_dictionary)
    return best_score
