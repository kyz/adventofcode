from collections import defaultdict

def count_orbits(orbits):
    objs = defaultdict(defaultdict)
    satellites = set()
    for orbit in orbits:
        objs[orbit[0]][orbit[1]] = objs[orbit[1]]
        satellites.add(orbit[1])
    count = lambda x, d: sum([count(objs[k], d+1) + d for k in x]) if x else 0
    return sum([count(objs[k], 1) for k in set(objs.keys()) - satellites])

def meet_santa(orbits):
    objs = dict()
    for orbit in orbits:
        objs[orbit[1]] = orbit[0]
    path1 = path_to_centre(objs, 'SAN')
    path2 = path_to_centre(objs, 'YOU')
    shared_dests = set(path1.keys()) & set(path2.keys())
    return min([path1[i] + path2[i] - 2 for i in shared_dests])

def path_to_centre(objs, body):
    path = dict()
    i = 0
    while body in objs:
        path[body] = i
        body = objs[body]
        i += 1
    return path

with open("day06.txt") as fh:
    orbits = [tuple(orbit.strip().split(')')) for orbit in fh.readlines()]
    print("2019 day 6 part 1: %d" % count_orbits(orbits))
    print("2019 day 6 part 2: %d" % meet_santa(orbits))
