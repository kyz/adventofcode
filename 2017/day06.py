with open("day06.txt") as f:
    data = [int(val) for val in f.readline().split()]
    cycles = 0
    seen = dict()
    while tuple(data) not in seen:
        seen[tuple(data)] = cycles
        v = max(data)
        i = data.index(v)
        data[i] = 0
        while v > 0:
            i = (i + 1) % len(data)
            data[i] += 1
            v -= 1
        cycles += 1
    print("2017 day 6 part 1: %d" % cycles)
    print("2017 day 6 part 2: %d" % (cycles - seen[tuple(data)]))
