def wire_positions(directions):
    compass = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    x, y, z = 0, 0, 0
    positions = dict()
    for d in directions:
        dx, dy = compass[d[0]]
        for dist in range(int(d[1:])):
            x += dx
            y += dy
            z += 1
            positions[x,y] = z
    return positions

def nearest_cross(p1, p2):
    crosses = set(p1.keys()) & set(p2.keys())
    return min([abs(pos[0]) + abs(pos[1]) for pos in crosses])

def best_cross(p1, p2):
    crosses = set(p1.keys()) & set(p2.keys())
    return min([p1[pos] + p2[pos] for pos in crosses])

with open("day03.txt") as fh:
    p1 = wire_positions([c for c in fh.readline().split(",")])
    p2 = wire_positions([c for c in fh.readline().split(",")])
    print("2019 day 3 part 1: %d" % nearest_cross(p1, p2))
    print("2019 day 3 part 2: %d" % best_cross(p1, p2))
