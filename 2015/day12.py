import json

def count_numbers(d, ignore=None):
    if type(d) is dict:
        vals = list(d.values())
        return 0 if ignore and ignore in vals else count_numbers(vals, ignore)
    if type(d) is list:
        return sum([count_numbers(v, ignore) for v in d])
    return d if type(d) is int else 0

with open("day12.txt") as fh:
    data = json.load(fh)
    print("2015 day 12 part 1: %d" % count_numbers(data))
    print("2015 day 12 part 2: %d" % count_numbers(data, "red"))
