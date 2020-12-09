try: xrange = xrange
except NameError: xrange = range

def part1(step):
    pos, buffer = 0, [0]
    for i in range(1, 2018):
        pos = (pos + step) % i + 1
        buffer.insert(pos, i)
    return buffer[buffer.index(2017) + 1]

def part2(step):
    pos, atpos1 = 0, None
    for i in xrange(1, 50000001):
        pos = (pos + step) % i + 1
        if pos == 1:
            atpos1 = i
    return atpos1

with open("day17.txt") as f:
    data = int(f.readline())
    print("2017 day 17 part 1: %d" % part1(data))
    print("2017 day 17 part 2: %d" % part2(data))
