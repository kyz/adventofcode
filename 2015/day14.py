class Reindeer(object):
    def __init__(self, line):
        p = line.split()
        self.speed = int(p[3])
        self.duration = int(p[6])
        self.rest = int(p[13])

    def dash(self):
        distance = 0
        while True:
            for i in range(self.duration):
                distance += self.speed
                yield distance
            for i in range(self.rest):
                yield distance

with open("day14.txt") as fh:
    data = [Reindeer(line) for line in fh]
    dash = [r.dash() for r in data]
    points = [0] * len(data)
    for secs in range(2503):
        dist = [next(d) for d in dash]
        furthest = max(dist)
        points[dist.index(furthest)] += 1
    print("2015 day 14 part 1: %d" % furthest)
    print("2015 day 14 part 2: %d" % max(points))
