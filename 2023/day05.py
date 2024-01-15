def read_almanac(fh):
    seeds = [int(x) for x in fh.readline().strip().split()[1:]]
    mappings, m = [], "dummy"
    while (line := fh.readline()):
        line = line.strip()
        if m is not None:
            if line: m.append([int(x) for x in line.split()])
            else: m = None
        else:
            m = []
            mappings.append(m)
    return seeds, mappings

def lowest_mapped(r):
    ranges = [r]
    for m in mappings:
        transformed = []
        for dest, src, length in m:
            ms, me = src, src + length
            new_ranges = []
            for r in ranges:
                rs, re = r[0], r[0] + r[1]
                if ms <= rs and me >= re:   # transform covers entire range
                    transformed += [(rs + dest - src, re - rs)]
                elif ms > rs and me < re:   # transform in middle of range
                    transformed += [(dest, length)]
                    new_ranges += [(rs, ms - rs), (me, re - me)]
                elif ms > rs and ms < re:   # transform overlaps end of range
                    transformed += [(dest, re - ms)]
                    new_ranges += [(rs, ms - rs)]
                elif me > rs and me < re:   # transform overlaps start of range
                    transformed += [(rs + dest - src, me - rs)]
                    new_ranges += [(me, re - me)]
                else:                       # transform does not apply
                    new_ranges += [r]
            ranges = new_ranges
        ranges += transformed
    return min(x[0] for x in ranges)

def paired(l):
    for i in range(0, len(l), 2): yield l[i], l[i+1]

with open("day05.txt", "r") as fh:
    seeds, mappings = read_almanac(fh)
    print("2023 day 05 part 1: %d" % min(lowest_mapped((s, 1)) for s in seeds))
    print("2023 day 05 part 2: %d" % min(lowest_mapped(r) for r in paired(seeds)))
