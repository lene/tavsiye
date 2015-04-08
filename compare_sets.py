from __future__ import division
from __future__ import print_function

__author__ = 'lene'

def jaccard_coefficient(set1, set2):
    return len(set1 & set2)/len(set1 | set2)

