import functools, operator

def answers(group, op):
    return functools.reduce(op, (set(p) for p in group.split("\n")))

with open("day06.txt", "r") as fh:
    groups = fh.read().strip().split("\n\n")
    print("2020 day 06 part 1: %d" % sum([len(answers(g, operator.or_)) for g in groups]))
    print("2020 day 06 part 1: %d" % sum([len(answers(g, operator.and_)) for g in groups]))
