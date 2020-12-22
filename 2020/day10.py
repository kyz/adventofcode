def diffs(adapters):
    one, three, prev = 0, 0, 0
    for j in adapters:
        if (j - prev) == 1: one += 1
        if (j - prev) == 3: three += 1
        prev = j
    return one * (three + 1)

def combos(adapters):
    adap = [0] + adapters # add power socket
    conn = {a: [c for c in range(a+1, a+4) if c in adap] for a in adap}
    combos = {adap[-1]: 1} # last adapter has 1 route
    for a in adap[-2::-1]: # reverse order, excluding last adapter
        combos[a] = sum([combos[c] for c in conn[a]])
    return combos[0] # number of combos from power socket

with open("day10.txt", "r") as fh:
    adapters = sorted([int(line) for line in fh.readlines()])
    print("2020 day 10 part 1: %d" % diffs(adapters))
    print("2020 day 10 part 2: %d" % combos(adapters))
