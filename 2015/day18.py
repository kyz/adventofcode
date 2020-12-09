def read_state(lines):
    out = dict()
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            out[x,y] = 1 if char == '#' else 0 
    return out, len(lines[0]), len(lines)

def simulate(state, w, h, corners):
    neighbours = {(x,y): [(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2)
        if i >= 0 and i < w and j >= 0 and j < h and (x,y) != (i,j)]
        for x,y in state}
    if corners:
        state[0,0] = state[w-1,0] = state[0,h-1] = state[w-1,h-1] = 1
    for c in range(100):
        newstate = dict()
        for s in state:
            n = sum([state[k] for k in neighbours[s]])
            newstate[s] = 1 if (n == 3 or (n == 2 and state[s])) else 0
        state = newstate
        if corners:
            state[0,0] = state[w-1,0] = state[0,h-1] = state[w-1,h-1] = 1
    return sum(state.values())

with open("day18.txt") as fh:
    state, w, h = read_state([l.strip() for l in fh.readlines()])
    print("2015 day 18 part 1: %d" % simulate(state, w, h, False))
    print("2015 day 18 part 2: %d" % simulate(state, w, h, True))
