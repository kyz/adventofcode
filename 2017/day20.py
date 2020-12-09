import re

def move(p):
    p[3] += p[6]; p[4] += p[7]; p[5] += p[8]
    p[0] += p[3]; p[1] += p[4]; p[2] += p[5]
    return (p[0], p[1], p[2])

def part1(data):
    particles = [[int(v) for v in p] for p in data]
    dist = [0] * len(particles)
    for tick in range(503):
        for i, p in enumerate(particles):
            posn = move(p)
            dist[i] += abs(posn[0]) + abs(posn[1]) + abs(posn[2])
    return dist.index(min(dist))

def part2(data):
    particles = [[int(v) for v in p] for p in data]
    dead = set()
    for tick in range(40):
        seen = {}
        for i, p in enumerate(particles):
            if i not in dead:
                posn = move(p)
                if posn in seen:
                    dead.add(i)
                    dead.add(seen[posn])
                seen[posn] = i
    return len(particles) - len(dead)

re1 = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")
with open("day20.txt") as f:
    data = [re1.match(line).groups() for line in f]
    print("2017 day 20 part 1: %d" % part1(data))
    print("2017 day 20 part 2: %d" % part2(data))
