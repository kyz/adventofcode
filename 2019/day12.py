import re
from gcd import lcm

def moon(line):
    return [int(x) for x in re.findall(r"(-?\d+)", line)] + [0,0,0]

def update(moons):
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            m = moons[i]; o = moons[j]
            for d in range(3):
                if   m[d] > o[d]: m[d+3] -= 1; o[d+3] += 1
                elif m[d] < o[d]: m[d+3] += 1; o[d+3] -= 1
    for m in moons:
        for d in range(3):
            m[d] += m[d+3]

def moon_energy(moons):
    moons = [list(m) for m in moons] # make a copy
    for x in range(1000):
        update(moons)
    return sum([(abs(m[0]) + abs(m[1]) + abs(m[2])) *
                (abs(m[3]) + abs(m[4]) + abs(m[5])) for m in moons])

def universe_repeats(moons):
    # find when there is a cycle in the x position and velocity of all moons,
    # and also for the y and z coordinates too
    seenx, seeny, seenz = set(), set(), set()
    findx, findy, findz = True, True, True
    while findx or findy or findz:
        x = tuple([(m[0], m[3]) for m in moons])
        y = tuple([(m[1], m[4]) for m in moons])
        z = tuple([(m[2], m[5]) for m in moons])
        if x in seenx: findx = False
        if y in seeny: findy = False
        if z in seenz: findz = False
        seenx.add(x); seeny.add(y); seenz.add(z)
        update(moons)
    # now we can say that the first cycle of all three elements is
    # the lowest common multiple of the three independent cycles
    return lcm(lcm(len(seenx), len(seeny)), len(seenz))

with open("day12.txt") as fh:
    moons = [moon(line) for line in fh.readlines()]
    print("2019 day 12 part 1: %d" % moon_energy(moons))
    print("2019 day 12 part 2: %d" % universe_repeats(moons))
