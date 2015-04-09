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

def minhash_similarity(set1, set2, length = 100):
    """
    An attempt at approximating the jaccard similarity with MinHash.
    Algorithm adapted from http://robertheaton.com/2014/05/02/jaccard-similarity-and-minhash-for-winners/
    Probably buggy, but passes my feeble attempts at testing.
    """
    (hashed1, hashed2) = (minhashed(set1, length), minhashed(set2, length))
    X = minhashed(hashed1 | hashed2, length)
    Y = X & hashed1 & hashed2
    return len(Y) / min(max(len(set1), len(set2)), length)


from random import randint
from sys import maxsize
def random_hash(item):
    return (randint(1, maxsize)+item)%maxsize

from operator import itemgetter
def minhashed(set, length = 100, hash_func = random_hash):
    indexable = list(set)
    min_item_indices  = []
    for i in range(length):
        index_and_hash = [(i, hash_func(indexable[i])) for i in range(len(indexable))]
        m = min(index_and_hash, key=itemgetter(1))
        min_item_indices.append(m[0])

    return { indexable[i] for i in min_item_indices }

