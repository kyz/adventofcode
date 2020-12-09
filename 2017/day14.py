from day10 import KnotHash

def hash(prefix, row):
    key = "%s-%d" % (prefix, row)
    hash = int(KnotHash().update(key).digest(), 16)
    return [1 if hash & 1 << (127-b) else 0 for b in range(128)]

def remove_groups(grid):
    count = 0
    for y in range(128):
        for x in range(128):
            if grid[y][x] == 1:
                remove_group(grid, x, y)
                count += 1
    return count

def remove_group(grid, x, y):
    if x >= 0 and x < 128 and y >= 0 and y < 128:
        if grid[y][x] == 1:
            grid[y][x] = 0
            remove_group(grid, x - 1, y)
            remove_group(grid, x + 1, y)
            remove_group(grid, x, y - 1)
            remove_group(grid, x, y + 1)

with open("day14.txt") as f:
    data = f.readline().strip()
    grid = [hash(data, row) for row in range(128)]
    print("2017 day 14 part 1: %d" % sum([sum(row) for row in grid]))
    print("2017 day 14 part 2: %d" % remove_groups(grid))
