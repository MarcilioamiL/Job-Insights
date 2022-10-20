from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        csv_read = csv.DictReader(file, delimiter=",", quotechar='"')
        csv_list = list(csv_read)
        return csv_list


"""Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
"""
