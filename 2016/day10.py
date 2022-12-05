import collections, re

def simulate(lines, part1):
    values = collections.defaultdict(list)
    rules = {}
    for line in lines:
        m1 = re.match(r"value (\d+) goes to bot (\d+)", line)
        m2 = re.match(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", line)
        if   m1: values[int(m1.group(2))].append(int(m1.group(1)))
        elif m2: rules[int(m2.group(1))] = [m2.group(2), int(m2.group(3)), m2.group(4), int(m2.group(5))]

    output = {}
    while values:
        for k in [k for k in values if len(values[k]) == 2]:
            if part1 and min(values[k]) == 17 and max(values[k]) == 61:
                return k
            lo1, lo2, hi1, hi2 = rules[k]
            if lo1 == "bot": values[lo2].append(min(values[k]))
            else:            output[lo2] = min(values[k])
            if hi1 == "bot": values[hi2].append(max(values[k]))
            else:            output[hi2] = max(values[k])
            del values[k]
    return output[0] * output[1] * output[2]

with open("day10.txt", "r") as fh:
    lines = [line.strip() for line in fh]
    print("2016 day 10 part 1: %d" % simulate(lines, True))
    print("2016 day 10 part 2: %d" % simulate(lines, False))
