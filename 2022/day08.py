dirs = [(0,-1),(1,0),(0,1),(-1,0)]

def read_map(fh):
    hmap = {}
    for y, line in enumerate(fh):
        for x, h in enumerate(line.strip()):
            hmap[x,y] = int(h)
    return hmap

def vis(hmap, x, y, dx, dy):
    h = hmap[x,y]; c = 0
    while True:
        x += dx; y += dy
        if (x,y) not in hmap:
            return (c, True) # reached edge of map
        c += 1
        if hmap[x,y] >= h:
            return (c, False) # didn't reach edge of map

def visible_trees(hmap):
    return sum(1 for x, y in hmap if max(vis(hmap, x, y, dx, dy)[1] for dx, dy in dirs))
def most_scenic(hmap):
    return max(score(hmap, x, y) for x, y in hmap)
def score(hmap, x, y):
    v = [vis(hmap, x, y, dx, dy)[0] for dx, dy in dirs]
    return v[0] * v[1] * v[2] * v[3]

with open("day08.txt", "r") as fh:
    hmap = read_map(fh)
    print("2022 day 08 part 1: %d" % visible_trees(hmap))
    print("2022 day 08 part 2: %d" % most_scenic(hmap))
