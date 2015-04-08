from __future__ import division
from __future__ import print_function

__author__ = 'lene'

def jaccard_coefficient(set1, set2):
    """
    A measure of similarity between two sets. Always between 0 (completely disjunct) and
    1 (containing the same elements).
    """
    return len(set1 & set2)/len(set1 | set2)

def naive_comparison(sets):
    """
    :param sets:    A list of sets. Jaccard distance is computed between each pair of sets.
    :return:        Matrix of jaccard distances between each pair of sets in the list.
    """
    return [ [ jaccard_coefficient(set1, set2) for set2 in sets] for set1 in sets ]

