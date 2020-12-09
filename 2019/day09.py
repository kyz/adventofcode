import intcode

def compute(program, inp):
    cpu = intcode.computer(program)
    next(cpu)
    return cpu.send(inp)

with open("day09.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 9 part 1: %d" % compute(p, 1))
    print("2019 day 9 part 2: %d" % compute(p, 2))
