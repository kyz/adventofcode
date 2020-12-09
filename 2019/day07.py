import intcode
from itertools import permutations

def run_amps(p, phases, once):
    amps = []
    for phase in phases:
        amp = intcode.computer(p) # or (p, 'cpu%d' % len(amps))
        next(amp) # get to first yield (input)
        amp.send(int(phase)) # provide first input and continue
        amps.append(amp)

    out = 0
    ended = False
    while not ended:
        for amp in amps:
            out = amp.send(out) # provide input, recieve output
            try: next(amp) # continue until next yield for input
            except StopIteration: ended = True
        if once: ended = True
    return out

def highest_amp_once(p):
    return max([run_amps(p, c, True) for c in permutations('01234', 5)])

def highest_amp_feedback(p):
    return max([run_amps(p, c, False) for c in permutations('56789', 5)])

with open("day07.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 7 part 1: %d" % highest_amp_once(p))
    print("2019 day 7 part 2: %d" % highest_amp_feedback(p))
