import collections

def read_paths(fh):
    paths = collections.defaultdict(set)
    for line in fh:
        src, dest = line.strip().split("-")
        if dest != "start": paths[src].add(dest)
        if src  != "start": paths[dest].add(src)
    return paths

def traverse(paths, extra_visit_allowed):
    can_visit = lambda n, visited: n.isupper() or n not in visited
    t = lambda path, visited, extra: 1 if path[-1] == "end" else sum(
        t(path + [n], visited | {n}, extra and can_visit(n, visited))
        for n in paths.get(path[-1], []) if can_visit(n, visited) or extra)
    return t(["start"], {"start"}, extra_visit_allowed)

with open("day12.txt", "r") as fh:
    paths = read_paths(fh)
    print("2021 day 12 part 1: %d" % traverse(paths, False))
    print("2021 day 12 part 2: %d" % traverse(paths, True))
