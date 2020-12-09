paper, ribbon = 0, 0
with open("day02.txt") as fh:
    for line in fh:
        l, w, h = sorted([int(val) for val in line.split("x")])
        paper += 2*l*w + 2*w*h + 2*h*l + l*w
        ribbon += 2*(l+w) + l*w*h
    print("2015 day 2 part 1: %d" % paper)
    print("2015 day 2 part 2: %d" % ribbon)

