import collections, re

def num_crossings(lines, orthagonal_only):
    grid = collections.defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = line
        if not orthagonal_only or (x1 == x2) or (y1 == y2):
            draw_line(grid, x1, y1, x2, y2)
    return sum(1 if grid[k] > 1 else 0 for k in grid)

def draw_line(grid, x1, y1, x2, y2):
    xstep = 0 if x1 == x2 else 1 if x1 < x2 else -1
    ystep = 0 if y1 == y2 else 1 if y1 < y2 else -1
    x, y = x1, y1
    while x != x2 or y != y2:
        grid[x, y] += 1
        x += xstep
        y += ystep
    grid[x2, y2] += 1

with open("day05.txt", "r") as fh:
    p = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    lines = [[int(i) for i in p.match(line).groups()] for line in fh]
    print("2021 day 05 part 1: %d" % num_crossings(lines, True))
    print("2021 day 05 part 2: %d" % num_crossings(lines, False))
