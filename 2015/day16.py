import re

def read_sue(line):
    name, data = re.match(r"Sue (\d+): (.+)", line).groups()
    sue = {"name": name}
    for d in data.split(", "):
        k, v = d.split(": ")
        sue[k] = int(v)
    return sue

def f1(x):
    def has(k, v): return k not in x or x[k] == v
    return (has("children", 3) and has("samoyeds", 2) and
            has("akitas", 0) and has("vizslas", 0) and
            has("cars", 2) and has("perfumes", 1) and
            has("cats", 7) and has("trees", 3) and
            has("pomeranians", 3) and has("goldfish", 5))

def f2(x):
    def has(k, v): return k not in x or x[k] == v
    def has_more(k, v): return k not in x or x[k] > v
    def has_less(k, v): return k not in x or x[k] < v
    return (has("children", 3) and has("samoyeds", 2) and
            has("akitas", 0) and has("vizslas", 0) and
            has("cars", 2) and has("perfumes", 1) and
            has_more("cats", 7) and has_more("trees", 3) and
            has_less("pomeranians", 3) and has_less("goldfish", 5))

with open("day16.txt") as fh:
    sues = [read_sue(line) for line in fh]
    sue1 = [s for s in sues if f1(s)][0]
    sue2 = [s for s in sues if f2(s)][0]
    print("2015 day 16 part 1: %s" % sue1["name"])
    print("2015 day 16 part 2: %s" % sue2["name"])
