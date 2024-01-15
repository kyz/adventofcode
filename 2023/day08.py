import itertools, math

def read_instructions(fh):
    instrs = fh.readline().strip()
    paths = {l[0:3]: {"L": l[7:10], "R": l[12:15]} for l in fh if l}
    return instrs, paths

def count_path(instrs, paths, start, end_reached):
    posn = start
    for step, instr in enumerate(itertools.cycle(instrs)):
        posn = paths[posn][instr]
        if end_reached(posn): return step + 1

def count_all_paths(instrs, paths):
    ends_z = lambda posn: posn.endswith("Z")
    lens = [count_path(instrs, paths, p, ends_z)
            for p in paths if p.endswith("A")]
    return math.lcm(*lens)

with open("day08.txt", "r") as fh:
    instrs, paths = read_instructions(fh)
    is_zzz = lambda posn: posn == "ZZZ"
    print("2023 day 08 part 1: %d" % count_path(instrs, paths, "AAA", is_zzz))
    print("2023 day 08 part 2: %d" % count_all_paths(instrs, paths))
