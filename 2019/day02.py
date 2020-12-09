def compute(p, noun, verb):
    p = list(p) # make a copy
    p[1] = noun
    p[2] = verb
    pc = 0
    while p[pc] != 99:
        (op, a, b, d) = p[pc : pc + 4]
        p[d] = p[a] + p[b] if op == 1 else p[a] * p[b]
        pc += 4
    return p[0]

def find_inputs(p):
    for noun in range(100):
        for verb in range(100):
            if compute(p, noun, verb) == 19690720:
                return 100 * noun + verb

with open("day02.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 2 part 1: %d" % compute(p, 12, 2))
    print("2019 day 2 part 2: %d" % find_inputs(p))
