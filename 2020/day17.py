import itertools

def simulate(lines, dimensions):
    grid = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                grid.add(tuple([x, y] + [0] * (dimensions - 2)))

    for cycle in range(6):
        newgrid = {}
        area = [range(min(c[d] for c in grid)-1,
                      max(c[d] for c in grid)+2) for d in range(dimensions)]
        for c in itertools.product(*area):
            neighbours = itertools.product(*[range(d-1, d+2) for d in c])
            n = sum(1 for nc in neighbours if nc in grid and nc != c)
            newgrid[c] = (n == 3) or (c in grid and n == 2)
        grid = {c for c in newgrid if newgrid[c]}

    return len(grid)

with open("day17.txt", "r") as fh:
    lines = fh.readlines()
    print("2020 day 17 part 1: %d" % simulate(lines, 3))
    print("2020 day 17 part 1: %d" % simulate(lines, 4))
