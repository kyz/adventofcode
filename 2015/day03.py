def deliver(directions):
    x, y, houses = 0, 0, set([(0,0)])
    for d in directions:
        if   d == ">": x += 1
        elif d == "<": x -= 1
        elif d == "v": y += 1
        elif d == "^": y -= 1
        houses.add((x, y))
    return houses

with open("day03.txt") as fh:
    directions = [d for d in fh.readline()]
    santa = deliver(directions[::2])
    robot = deliver(directions[1::2])
    print("2015 day 3 part 1: %d" % len(deliver(directions)))
    print("2015 day 3 part 2: %d" % len(santa | robot))
