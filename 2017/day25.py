from collections import defaultdict

def build_turing_machine(data):
    initial_state = data[0].split()[-1].rstrip(".")
    iterations = int(data[1].split()[-2])
    conditions = {}
    for i in range(2, len(data)-1, 10):
        state =       data[i+1].split()[-1].rstrip(":")
        write0 = int( data[i+3].split()[-1].rstrip("."))
        move0 = -1 if data[i+4].split()[-1] == "left." else 1
        state0 =      data[i+5].split()[-1].rstrip(".")
        write1 = int( data[i+7].split()[-1].rstrip("."))
        move1 = -1 if data[i+8].split()[-1] == "left." else 1
        state1 =      data[i+9].split()[-1].rstrip(".")
        conditions[(state, 0)] = (write0, move0, state0)
        conditions[(state, 1)] = (write1, move1, state1)
    return initial_state, iterations, conditions

with open("day25.txt") as f:
    data = f.readlines()
    state, iterations, conds = build_turing_machine(data)
    tape, pos = defaultdict(int), 0
    for i in range(iterations):
        write, move, newstate = conds[(state, tape[pos])]
        tape[pos] = write
        pos += move
        state = newstate
    print("2017 day 25: %d" % sum(tape.values()))
