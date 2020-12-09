def molecules(formula, replacements):
    for (s, r) in replacements:
        start = 0
        while (i := formula.find(s, start)) > -1:
            start = i + len(s)
            yield formula[:i] + r + formula[start:]

def steps_needed(medicine, replacements):
    # go from full medicine backwards to "e",
    # only keeping the "N" shortest replacements
    n = 1
    rr = [(r, s) for (s, r) in replacements]
    seen = set()
    steps = 0
    current = [medicine]
    while "e" not in seen:
        todo = set()
        for c in current:
            todo |= set(molecules(c, rr))
        # keep only the shortest results
        current = sorted(todo, key=len)[:n]
        seen |= todo
        steps += 1
    return steps

with open("day19.txt") as fh:
    lines = [line.strip() for line in fh]
    replacements = [line.split(" => ") for line in lines[:-2]]
    medicine = lines[-1]
    print("2015 day 19 part 1: %d" % len(set(molecules(medicine, replacements))))
    print("2015 day 19 part 2: %d" % steps_needed(medicine, replacements))

