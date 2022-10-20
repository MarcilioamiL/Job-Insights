from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as f:
        csv_read = csv.DictReader(f, delimiter=",", quotechar='"')
        csv_list = list(csv_read)
        return csv_list
