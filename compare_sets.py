__author__ = 'lene'


from typing import Set, List
from typedefs import Item, User, LikedItems, SimilarityFunction, SimilarityMatrix

"""
Usage example:
>>> from read_file import read_file
>>> sets = read_file('testdata.csv')
>>> similarity = similarity_matrix(sets)
>>> user = 1
>>> cutoff = 0.25
>>> print(recommendations(user, sets, similarity, cutoff))
"""


def jaccard_coefficient(set1: Set[Item], set2: Set[Item]) -> float:
    """
    A measure of similarity between two sets. Always between 0 (completely disjunct) and
    1 (containing the same elements).
    """
    return len(set1 & set2) / len(set1 | set2)


def similarity_matrix(
        liked_items: LikedItems, similarity: SimilarityFunction=jaccard_coefficient
) -> SimilarityMatrix:
    return {
        user1: {
            user2: similarity(set1, set2) for (user2, set2) in liked_items.items()
        } for (user1, set1) in liked_items.items()
    }


def similar_users(user: User, user_similarity: SimilarityMatrix, cutoff: float) -> List[User]:
    return [
        other_user
        for other_user in user_similarity[user]
        if user != other_user and user_similarity[user][other_user] >= cutoff
    ]


def recommendations(
        user: User, liked_items: LikedItems, user_similarity: SimilarityMatrix,
        cutoff: float
) -> Set[Item]:
    return {
        item
        for similar in similar_users(user, user_similarity, cutoff)
        for item in liked_items[similar] - liked_items[user]
    }
