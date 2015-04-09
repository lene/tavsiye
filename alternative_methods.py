from __future__ import division

__author__ = 'lene'

def asymmetric_similarity(set1, set2):
    """
    Here's an idea for a different metric for similarity: We are not interested in the length of
    set2, only of set1. This implies that this function is not commutative.
    In terms of the problem that means, roughly, a user is only interested if another user shares their
    preferences - not if they share the other user's preferences as well.
    """
    return len(set1 & set2)/len(set1)
