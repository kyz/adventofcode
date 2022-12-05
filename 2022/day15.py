import re
SENSOR = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

def manhattan_distance(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def known_empty(sensors, y):
    known_beacons, known_ranges = set(), set()
    for sx, sy, bx, by in sensors:
        # find the range of x coords on line y that are within the
        # manhattan distance between (sx,sy) and (bx,by)
        xrange = manhattan_distance(sx, sy, bx, by) - abs(y - sy)
        if xrange >= 0: known_ranges.add((sx - xrange, sx + xrange))
        # remember beacons if they're on line y
        if by == y: known_beacons.add(bx)
    # count the known ranges of no-beacons, excluding overlaps
    count, prev_hi = 0, -99999
    for r in sorted(known_ranges, key=lambda r: r[0]):
        if r[1] > prev_hi:
            count += r[1] - max(r[0], prev_hi + 1) + 1
            prev_hi = r[1]
    # remove any known beacons if they're within a range we've counted
    for b in known_beacons:
        for r in known_ranges:
            if b >= r[0] and b <= r[1]:
                count -= 1 
                break
    return count

def find_missing_beacon(sensors, l, h):
    ac, bc = set(), set()
    md = {}
    for sx, sy, bx, by in sensors:
        md[sx,sy] = manhattan_distance(sx, sy, bx, by)
        ac.add(sy - sx + md[sx,sy] + 1) # 1 pixel outside top/left edge
        ac.add(sy - sx - md[sx,sy] - 1) # 1 pixel outside bottom/right edge
        bc.add(sx + sy + md[sx,sy] + 1) # 1 pixel outside top/right edge
        bc.add(sx + sy - md[sx,sy] - 1) # 1 pixel outside bottom/left edge
    # check all intersections of these 1-pixel-outside sensor radius lines
    for a in ac:
        for b in bc:
            x, y = (b-a)//2, (a+b)//2 # intersection point
            if l <= x <= h and l <= y <= h: # is point within boundary?
                beyond_all = True
                for sx, sy, bx, by in sensors:
                    beyond_all &= manhattan_distance(x, y, sx, sy) > md[sx,sy]
                if beyond_all: # is this point beyond ALL sensors?
                    return x * 4000000 + y

with open("day15.txt", "r") as fh:
    sensors = [list(map(int, m.groups())) for m in re.finditer(SENSOR, fh.read())]
    print("2022 day 15 part 1: %d" % known_empty(sensors, 2000000))
    print("2022 day 15 part 2: %d" % find_missing_beacon(sensors, 0, 4000000))

