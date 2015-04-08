__author__ = 'lene'

import csv

def read_file(filename):
    """
    reads a file containing CSV of the form "user_id;product_id"
    :param filename:    name of the file (duh)
    :return:            a dict of the form { user_id: [product_id, ...], ... }
    """
    return read_from_reader(csv.reader(open(filename), delimiter=';'))

def read_from_reader(reader):
    values = {}
    for row in reader:
        values[int(row[0])] = values[int(row[0])] | {int(row[1])} if int(row[0]) in values else {int(row[1])}

    return values

