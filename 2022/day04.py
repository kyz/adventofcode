def parse_ranges(s):
    return tuple(int(x) for x in s.replace(",", " ").replace("-", " ").split())

def contained(r):
    return (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1])

def overlap(r):
    return contained(r) or (r[0] >= r[2] and r[0] <= r[3]) or (r[1] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[2] <= r[1]) or (r[3] >= r[0] and r[3] <= r[1])

def count(ranges, fn):
    return sum(1 if fn(r) else 0 for r in ranges)

with open("day04.txt", "r") as fh:
    ranges = [parse_ranges(l) for l in fh.readlines()]
    print("2022 day 04 part 1: %d" % count(ranges, contained))
    print("2022 day 04 part 2: %d" % count(ranges, overlap))




