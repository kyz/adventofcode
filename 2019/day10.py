from math import atan2
from collections import defaultdict
from itertools import cycle

def read_grid(lines):
    return set([(x, y) for x in range(len(lines[0]))
                       for y in range(len(lines)) if lines[y][x] == '#'])

# returns a dict where the key is the slope from o to another point in
# grid, and the value is the list of all points that share that slope,
# ordered from nearest (to o) to furthest
def view(o, grid):
    out = defaultdict(list)
    for n in grid - {o}:
        slope = atan2(n[0] - o[0], n[1] - o[1])
        out[slope].append(n)
    for k in out:
        out[k].sort(key=lambda x: (x[0]-o[0])**2 + (x[1]-o[1])**2)
    return out

def frikkin_lasers(view, stop_at):
    # go around in a clockwise circle of slopes, from directly up
    # (slope=pi) to bottom (slope=0) to up again (slope=-pi)
    slopes = cycle(sorted(view.keys(), reverse=True))
    latest = None
    while stop_at > 0:
        s = next(slopes)
        if view[s]:
            # remove the nearest thing with this slope into latest
            latest, view[s] = view[s][0], view[s][1:]
            stop_at -= 1
    return latest[0] * 100 + latest[1]

with open("day10.txt") as fh:
    grid = read_grid(fh.readlines())
    best = max([view(o, grid) for o in grid], key=len)
    print("2019 day 10 part 1: %d" % len(best))
    print("2019 day 10 part 2: %d" % frikkin_lasers(best, 200))
