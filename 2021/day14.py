import collections

def read_rules(fh):
    template, _blank = fh.readline().strip(), fh.readline()
    rules = {l.split()[0]: l.split()[2] for l in fh}
    return template, rules

def expand(s, rules, rounds):
    pairs = collections.defaultdict(int)
    for i in range(len(s)-1):
        pairs[s[i:i+2]] += 1

    for i in range(rounds):
        newpairs = collections.defaultdict(int)
        for k in pairs:
            if rules[k]:
                newpairs[k[0] + rules[k]] += pairs[k]
                newpairs[rules[k] + k[1]] += pairs[k]
            else:
                newpairs[k] += pairs[k]
        pairs = newpairs

    singles = collections.defaultdict(int)
    for k in pairs:
        singles[k[0]] += pairs[k]
    singles[s[-1]] += 1 # include the last character (never substituted)

    out = sorted(singles.values())
    return out[-1] - out[0]

with open("day14.txt", "r") as fh:
    template, rules = read_rules(fh)
    print("2021 day 14 part 1: %d" % expand(template, rules, 10))
    print("2021 day 14 part 2: %d" % expand(template, rules, 40))


