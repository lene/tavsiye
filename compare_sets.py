from __future__ import division
from __future__ import print_function

__author__ = 'lene'


def jaccard_coefficient(set1, set2):
    """
    A measure of similarity between two sets. Always between 0 (completely disjunct) and
    1 (containing the same elements).
    """
    return len(set1 & set2)/len(set1 | set2)

def similarity_matrix(sets, similarity = jaccard_coefficient):
    """
    :param sets:        A dict of sets. Similarity is computed between each pair of sets.
    :param similarity:  Function to compute similarity between two sets. Defaults to jaccard_coefficient.
    :return:            Two-dimensional dict of jaccard distances between each pair of sets, indexed with the user
    """
    return {
        user1: {
            user2: similarity(set1, set2) for (user2, set2) in sets.items()
        } for (user1, set1) in sets.items()
    }

def similar_users(user, similarity_matrix, cutoff):
    return [ other_user for other_user in similarity_matrix[user]
                        if user != other_user and similarity_matrix[user][other_user] >= cutoff ]

def recommendations(user, sets, similarity_matrix, cutoff):
    return { item for similar in similar_users(user, similarity_matrix, cutoff)
                  for item in sets[similar] - sets[user] }
