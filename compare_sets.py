from __future__ import division
from __future__ import print_function

__author__ = 'lene'

from read_file import read_file
from collections import OrderedDict

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

def comparison_with_dict(sets):
    """
    :param sets:    A dict of sets. Jaccard distance is computed between each pair of sets.
    :return:        Two-dimensional dict of jaccard distances between each pair of sets, indexed with the user
    """
    return {
        user1: {
            user2: jaccard_coefficient(set1, set2) for (user2, set2) in sets.items()
        } for (user1, set1) in sets.items()
    }

if __name__ == '__main__':

    print(comparison_with_dict(read_file('testdata.csv')))