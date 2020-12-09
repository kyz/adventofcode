from collections import defaultdict

def count_infected(data, steps, mutate):
    grid = defaultdict(lambda: ".")
    cx, cy = len(data[0]) >> 1, len(data) >> 1
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x-cx,y-cy)] = c

    turns = {"#": 1, ".": -1, "W": 0, "F": 2}
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    d, infected, pos = 0, 0, (0,0)
    for i in range(steps):
        d = (d + turns[grid[pos]]) % len(dirs)
        grid[pos] = mutate[grid[pos]]
        if grid[pos] == "#":
            infected += 1
        pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
    return infected

with open("day22.txt") as f:
    data = [line.strip() for line in f]
    mut1 = {".": "#", "#": "."}
    mut2 = {".": "W", "#": "F", "W": "#", "F": "."}
    print("2017 day 22 part 1: %d" % count_infected(data, 10000, mut1))
    print("2017 day 22 part 1: %d" % count_infected(data, 10000000, mut2))
