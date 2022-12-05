def draw_cave(lines):
    cave = set()
    for line in lines:
        coords = line.strip().split(" -> ")
        ox, oy = map(int, coords[0].split(","))
        for i in range(1, len(coords)):
            x, y = map(int, coords[i].split(","))
            if x != ox: cave |= {(j,y) for j in range(min([ox, x]), max([ox, x])+1)}
            if y != oy: cave |= {(x,j) for j in range(min([oy, y]), max([oy, y])+1)}
            ox, oy = x, y
    return cave

def add_sand(cave, part1):
    grains = 0
    floor = max(y for x,y in cave)
    while True:
        x, y = 500, 0
        if (x,y) in cave: return grains # exit point for part 2
        while True:
            if y > floor:
                if part1: return grains # exit point for part 1
                cave.add((x,y))
                break
            elif (x, y+1) not in cave:
                y += 1
            elif (x-1, y+1) not in cave:
                x -= 1; y += 1
            elif (x+1, y+1) not in cave:
                x += 1; y += 1
            else: # can't move
                cave.add((x,y))
                break
        grains += 1

with open("day14.txt", "r") as fh:
    cave = draw_cave(fh.readlines())
    print("2022 day 14 part 1: %d" % add_sand(set(cave), True))
    print("2022 day 14 part 2: %d" % add_sand(set(cave), False))

