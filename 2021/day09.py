import functools, operator

def read_map(fh):
    hmap = {}
    for y, line in enumerate(fh):
        for x, h in enumerate(line.strip()):
            hmap[x,y] = int(h)
    return hmap

def neighbours(k):
    return [(k[0],k[1]+1), (k[0],k[1]-1), (k[0]+1,k[1]), (k[0]-1,k[1])]

def low_point(hmap, k):
    return functools.reduce(operator.and_, (hmap[k] < hmap.get(n, 10) for n in neighbours(k)))

def risk_map(hmap):
    return sum(1 + hmap[k] for k in hmap if low_point(hmap, k))

def basin_size(hmap, k, seen=set()):
    if k in seen or k not in hmap or hmap[k] == 9:
        return 0
    else:
        seen.add(k)
        return 1 + sum(basin_size(hmap, n, seen) for n in neighbours(k))

def basin_sizes(hmap):
    sizes = sorted(basin_size(hmap, k) for k in hmap if low_point(hmap, k))
    return sizes[-1] * sizes[-2] * sizes[-3]

with open("day09.txt", "r") as fh:
    hmap = read_map(fh)
    print("2021 day 09 part 1: %d" % risk_map(hmap))
    print("2021 day 09 part 2: %d" % basin_sizes(hmap))
