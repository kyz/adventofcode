from collections import defaultdict
from itertools import cycle, count
# Python 3 got rid of itertools.izip because zip now does it (but not in Python 2)
try: from itertools import izip
except: izip = zip

def spiral_directions():
    dirs  = cycle([(1,0), (0,-1), (-1,0), (0,1)]) # R, U, L, D, ...
    dists = (n >> 1 for n in count(2)) # 2, 2, 3, 3, 4, 4, 5, 5, ...
    return izip(dists, dirs)

def distance_to_square(square):
    square -= 1
    x, y = 0, 0
    for d in spiral_directions():
        dist = min(d[0], square)
        x += dist * d[1][0]
        y += dist * d[1][1]
        square -= dist
        if square == 0:
            return abs(x) + abs(y)

def first_square_over(threshold):
    mem = defaultdict(int)
    x, y, mem[0, 0] = 0, 0, 1
    for d in spiral_directions():
        for i in range(d[0]):
            x += d[1][0]
            y += d[1][1]
            mem[x, y] = sum([mem[j, k] for j in range(x-1, x+2)
                                       for k in range(y-1, y+2)])
            if mem[x, y] > threshold:
                return mem[x, y]

with open("day03.txt") as f:
    data = int(f.readline())
    print("2017 day 3 part 1: %d" % distance_to_square(data))
    print("2017 day 3 part 2: %d" % first_square_over(data))
