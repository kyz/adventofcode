import re

p = re.compile(r"\((\d+)x(\d+)\)")

def parse(s):
    segs, i, m = [], 0, p.search(s)
    while m:
        start, end = m.start(0)+i, m.end(0)+i
        len_, reps = int(m.group(1)), int(m.group(2))
        segs.append((1, s[i:start]))
        segs.append((reps, s[end:end+len_]))
        i = end + len_
        m = p.search(s[i:])
    segs.append((1, s[i:]))
    return segs

def decompress(packed):
    return sum(s[0] * len(s[1]) for s in parse(packed))

def decompress2(packed):
    segs = parse(packed)
    return (len(segs[0][1]) if len(segs) == 1 and segs[0][0] == 1
        else sum(s[0] * decompress2(s[1]) for s in segs))

with open("day09.txt", "r") as fh:
    packed = fh.readline().strip()
    print("2016 day 09 part 1: %d" % decompress(packed))
    print("2016 day 09 part 2: %d" % decompress2(packed))

