import intcode

def compute(p, inp):
    cpu = intcode.computer(p)
    next(cpu)
    result = cpu.send(inp)
    while result == 0:
        result = next(cpu)
    return result

with open("day05.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 5 part 1: %d" % compute(p, 1))
    print("2019 day 5 part 2: %d" % compute(p, 5))
