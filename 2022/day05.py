def read_config(fh):
    part1, part2 = [l.split("\n") for l in fh.read().rstrip().split("\n\n")]
    w, h = (len(part1[0]) + 1) // 4, len(part1) - 1
    stacks = [list() for x in range(w)]
    for y in range(h):
        for x in range(w):
            c = part1[h-1-y][1+x*4]
            if c != ' ':
                stacks[x].append(c)
    moves = [tuple(int(x) for x in p.split()[1::2]) for p in part2]
    return stacks, moves

def apply_moves(stacks, moves, in_order):
    stacks = [list(x) for x in stacks] # make a copy
    for m in moves:
        temp = [stacks[m[1]-1].pop() for x in range(m[0])]
        stacks[m[2]-1].extend(reversed(temp) if in_order else temp)
    return "".join(x.pop() for x in stacks)

with open("day05.txt", "r") as fh:
    stacks, moves = read_config(fh)
    print("2022 day 05 part 1: %s" % apply_moves(stacks, moves, False))
    print("2022 day 05 part 2: %s" % apply_moves(stacks, moves, True))
