from __future__ import division
from __future__ import print_function

__author__ = 'lene'

def jaccard_coefficient(set1, set2):
    return len(set1 & set2)/len(set1 | set2)

def naive_comparison(sets):
    return [ [ jaccard_coefficient(set1, set2) for set2 in sets] for set1 in sets ]

