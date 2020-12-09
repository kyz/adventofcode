def trees_hit(grid, xi, yi):
    w, h = len(grid[0]), len(grid)
    trees = {(x, y) for x in range(w) for y in range(h) if grid[y][x] == '#'}

    x, y, count = 0, 0, 0
    while y < h:
        if (x % w, y) in trees: count += 1
        x += xi
        y += yi
    return count

def total_hits(grid):
    return (trees_hit(grid, 1, 1) *
            trees_hit(grid, 3, 1) *
            trees_hit(grid, 5, 1) *
            trees_hit(grid, 7, 1) *
            trees_hit(grid, 1, 2))

with open("day03.txt", "r") as fh:
    grid = [line.strip() for line in fh.readlines()]
    print("2020 day 03 part 1: %d" % trees_hit(grid, 3, 1))
    print("2020 day 03 part 2: %d" % total_hits(grid))
