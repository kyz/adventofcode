from collections import defaultdict
from operator import lt, le, eq, ne, ge, gt

regs = defaultdict(int)
comparator = {"<": lt, "<=": le, "==": eq, "!=": ne, ">=": ge, ">": gt}
highest = []
with open("day08.txt") as f:
    for line in f:
        reg1, incdec, val, _if, reg2, test, operand = line.split()
        if comparator[test](regs[reg2], int(operand)):
            regs[reg1] += int(val) * (1 if incdec == "inc" else -1)
            highest.append(max(regs.values()))

    print("2017 day 8 part 1: %d" % highest[-1])
    print("2017 day 8 part 2: %d" % max(highest))
