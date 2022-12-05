from itertools import islice

def computer(program):
    pc, v = 0, 1
    while True:
        if program[pc][0] == "noop":
            yield v
        else:
            yield v; yield v; v += int(program[pc][1])
        pc = (pc + 1) % len(program)

def signal_strength(program):
    cpu = computer(program)
    return sum(islice((c*(i+1) for i, c in enumerate(cpu)), 19, 220, 40))

def show_sprite(program):
    cpu = computer(program)
    pixel = lambda x, v: "██" if v >= (x-1) and v <= (x+1) else "  "
    for y in range(6): print("".join([pixel(x, next(cpu)) for x in range(40)]))

with open("day10.txt", "r") as fh:
    program = [line.split() for line in fh]
    print("2022 day 10 part 1: %d" % signal_strength(program))
    print("2022 day 10 part 2:"); show_sprite(program)

