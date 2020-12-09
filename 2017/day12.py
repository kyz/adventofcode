from functools import reduce

def group(n):
    oldlen = 0
    grp = set([n])
    while len(grp) != oldlen:
        oldlen = len(grp)
        grp |= reduce(lambda x, y: x | y, [deps[x] for x in grp])
    return grp

def count_groups(d):
    count = 0
    while len(d) > 0:
        for x in group(list(d.keys())[0]):
            del d[x]
        count += 1
    return count

deps = dict()
with open("day12.txt") as f:
    for line in f:
        p = line.split(" <-> ")
        deps[int(p[0])] = frozenset([int(n) for n in p[1].split(", ")])
    print("2017 day 12 part 1: %d" % len(group(0)))
    print("2017 day 12 part 2: %d" % count_groups(deps))
