def chart_course(directions):
    hpos, depth = 0, 0
    for d in directions:
        if d[0] == "forward":
            hpos += int(d[1])
        elif d[0] == "up":
            depth -= int(d[1])
        elif d[0] == "down":
            depth += int(d[1])
    return hpos * depth

def chart_aim(directions):
    hpos, depth, aim = 0, 0, 0
    for d in directions:
        if d[0] == "forward":
            hpos += int(d[1])
            depth += int(d[1]) * aim
        elif d[0] == "up":
            aim -= int(d[1])
        elif d[0] == "down":
            aim += int(d[1])
    return hpos * depth


with open("day02.txt", "r") as fh:
    directions = [line.strip().split() for line in fh.readlines()]
    print("2021 day 02 part 1: %d" % chart_course(directions))
    print("2021 day 02 part 2: %d" % chart_aim(directions))
