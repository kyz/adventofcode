dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def neighbours(f, grid):
    w, h = grid["size"]
    return {(x,y): f(grid, x, y) for x in range(w) for y in range(h)}

def immediate(grid, x, y):
    return [(x+d[0],y+d[1]) for d in dirs if grid.get((x+d[0],y+d[1])) is not None]

def nearest(grid, x, y):
    out = []
    for d in dirs:
        pos = (x + d[0], y + d[1])
        while grid.get(pos) == '.':
            pos = (pos[0] + d[0], pos[1] + d[1])
        if pos in grid:
            out.append(pos)
    return out

def occupied(grid, adjacent, t):
    prev = None
    while grid != prev:
        prev = grid.copy()
        for x in range(grid["size"][0]):
            for y in range(grid["size"][1]):
                n = sum(1 for a in adjacent[x,y] if prev[a] == '#')
                if   grid[x,y] == 'L' and n == 0: grid[x,y] = '#'
                elif grid[x,y] == '#' and n >= t: grid[x,y] = 'L'
    return sum(1 for c in grid.values() if c == '#')

def parse(lines):
    w, h = len(lines[0]), len(lines)
    grid = {(x,y): lines[y][x] for x in range(w) for y in range(h)}
    grid["size"] = (w, h)
    return grid

with open("day11.txt", "r") as fh:
    grid = parse([line.strip() for line in fh.readlines()])
    print("2020 day 11 part 1: %d" % occupied(grid.copy(), neighbours(immediate, grid), 4))
    print("2020 day 11 part 2: %d" % occupied(grid.copy(), neighbours(nearest, grid), 5))
