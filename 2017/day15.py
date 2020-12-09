def generator(factor, val, mask):
    while True:
        val = (val * factor) % 2147483647
        if val & mask == 0:
            yield val

def matches(gena, genb, count):
    return sum([1 if (next(gena) & 65535) == (next(genb) & 65535) else 0
                for x in range(count)])

with open("day15.txt") as f:
    data = [int(line.split()[-1]) for line in f]
    gena = generator(16807, data[0], 0)
    genb = generator(48271, data[1], 0)
    print("2017 day 15 part 1: %d" % matches(gena, genb, 40000000))
    gena = generator(16807, data[0], 3)
    genb = generator(48271, data[1], 7)
    print("2017 day 15 part 2: %d" % matches(gena, genb, 5000000))
