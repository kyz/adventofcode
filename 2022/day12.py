def read_map(fh):
    hmap = {}
    for y, line in enumerate(fh):
        for x, h in enumerate(line.strip()):
            hmap[x,y] = ord(h) - ord("a")
            if   h == "S": start = (x,y)
            elif h == "E": end = (x,y)
    hmap[start] = 0; hmap[end] = 25
    return hmap, start, end

def distance(hmap, start, end):
    dist = {}
    cur = {start}
    d = 0
    while cur:
        todo = set()
        for c in cur:
            dist[c] = d
            x,y = c
            for n in [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]:
                if n in hmap and hmap[n] <= hmap[c]+1 and n not in dist:
                    todo.add(n)
        d += 1
        cur = todo
    return dist[end]

def nearest_b(hmap, start, end):
    return min(distance(hmap, b, end) for b in hmap if hmap[b] == 1) + 1

with open("day12.txt", "r") as fh:
    hmap, start, end = read_map(fh)
    print("2022 day 12 part 1: %d" % distance(hmap, start, end))
    print("2022 day 12 part 2: %d" % nearest_b(hmap, start, end))
