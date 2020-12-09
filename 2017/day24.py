from collections import defaultdict

def bridges(existing=set(), lookup=0):
    out = []
    for part in parts[lookup]:
        if part not in existing:
            bridge = existing | {part}
            strength = sum([p[0] + p[1] for p in bridge])
            out.append((len(bridge), strength, bridge))
            out += bridges(bridge, part[1] if lookup == part[0] else part[0])
    return out

with open("day24.txt") as f:
    data = [line.strip() for line in f]

    parts = defaultdict(set)
    for part in data:
        a, b = sorted([int(n) for n in part.split("/")])
        parts[a].add((a,b))
        parts[b].add((a,b))

    bridges = bridges()
    bystr = lambda x: x[1]
    print("2017 day 24 part 1: %d" % sorted(bridges, key=bystr)[-1][1])
    print("2017 day 24 part 2: %d" % sorted(bridges)[-1][1])
