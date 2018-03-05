
import random
import operator

from typing import List, Tuple
from typedefs import User, Item

UserFavoriteList = List[Tuple[User, List[Item]]]  # [(user1, [item1, ...), ...]


def minhash(users: UserFavoriteList, length: int, seed: int=None) -> UserFavoriteList:
    random.seed(seed)
    return [(user, get_min_seq_items(items, length)) for user, items in users]


def get_min_seq_items(items: List[Item], length: int) -> List[Item]:
    return [items[i] for i in get_min_seq(length, len(items))]


def get_min_seq(minhash_length: int, actual_length: int) -> List[int]:
    return [get_min_random_index(actual_length) for _ in range(minhash_length)]


def get_min_random_index(actual_length: int) -> int:
    seqs = [(i, random.randint(1, 10 ** 6)) for i in range(actual_length)]
    return min(seqs, key=operator.itemgetter(1))[0]
