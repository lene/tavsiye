__author__ = 'lene'

from random import randint
from sys import maxsize
from operator import itemgetter
from typing import Set, Callable, Sequence

from typedefs import Item


HashFunction = Callable[[Item], int]


def asymmetric_similarity(set1: Set[Item], set2: Set[Item]) -> float:
    """
    Here's an idea for a different metric for similarity: We are not interested in the length of
    set2, only of set1. This implies that this function is not commutative.
    In terms of the problem that means, roughly, a user is only interested if another user shares
    their preferences - not if they share the other user's preferences as well.
    """
    return len(set1 & set2) / len(set1)


def minhash_similarity(set1: Set[Item], set2: Set[Item], length: int=100) -> float:
    """
    An attempt at approximating the jaccard similarity with MinHash.
    Algorithm adapted from
    http://robertheaton.com/2014/05/02/jaccard-similarity-and-minhash-for-winners/
    Probably buggy, but passes my feeble attempts at testing.
    """
    (hashed1, hashed2) = (minhashed(set1, length), minhashed(set2, length))
    x = minhashed(hashed1 | hashed2, length)
    y = x & hashed1 & hashed2
    return len(y) / min(max(len(set1), len(set2)), length)


def random_hash(item: Item) -> int:
    return (randint(1, maxsize) + item) % maxsize


def minhashed(data: Set[Item], length: int=100, hash_func: HashFunction=random_hash):
    indexable = list(data)
    min_item_indices = [min_item_index(hash_func, indexable)[0] for _ in range(length)]
    return {indexable[i] for i in min_item_indices}


def min_item_index(hash_func: HashFunction, indexable: Sequence[Item]):
    index_and_hash = [(i, hash_func(indexable[i])) for i in range(len(indexable))]
    return min(index_and_hash, key=itemgetter(1))
