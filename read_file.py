__author__ = 'lene'

import csv
from collections import defaultdict

from typedefs import LikedItems


def read_file(filename: str) -> LikedItems:
    """
    reads a file containing CSV of the form "user_id;product_id"
    """
    with open(filename) as file:
        reader = csv.reader(file, delimiter=';')
        values = defaultdict(set)  # type: LikedItems
        for row in reader:
            values[int(row[0])].add(int(row[1]))

        return values
