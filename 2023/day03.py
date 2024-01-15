import collections, re

def parse_schematic(schematic):
    w, h = len(schematic[0]), len(schematic)
    parts, gears = list(), collections.defaultdict(list)

    def add(x, y):
        if 0 < x < w and 0 < y < h:
            syms.add(schematic[y][x])
            if schematic[y][x] == "*":
                gears[x, y].append(part)

    for y, line in enumerate(schematic):
        for m in re.finditer(r"\d+", line):
            part = int(m.group())
            x0, x1 = m.span()
            syms = set()
            add(x0-1, y); add(x1, y) # left and right
            for x in range(x0-1, x1+1):
                add(x, y-1); add(x, y+1) # top and bottom
            parts.append((part, syms - {".", "\n"}))

    return parts, gears.values()

with open("day03.txt", "r") as fh:
    parts, gears = parse_schematic(fh.readlines())
    print("2023 day 03 part 1: %d" % sum(p[0] for p in parts if p[1]))
    print("2023 day 03 part 2: %d" % sum(g[0]*g[1] for g in gears if len(g) > 1))
