__author__ = 'lene'

import csv
from collections import defaultdict


def read_file(filename):
    """
    reads a file containing CSV of the form "user_id;product_id"
    :param filename:    name of the file (duh)
    :return:            a dict of the form { user_id: [product_id, ...], ... }
    """
    with open(filename) as file:
        return read_from_reader(csv.reader(file, delimiter=';'))


def read_from_reader(reader):
    values = defaultdict(set)
    for row in reader:
        values[int(row[0])] |= {int(row[1])}

    return values
