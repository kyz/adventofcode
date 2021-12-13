import re

def read_instructions(fh):
    a, b = fh.read().strip().split("\n\n")
    paper = {tuple(int(x) for x in l.split(",")) for l in a.split("\n")}
    instr = [re.search("(x|y)=(\d+)", l).groups() for l in b.split("\n")]
    return paper, instr

def fold(paper, instructions):
    for coord, line in instructions:
        x = int(line)
        fold = lambda y: y if y < x else x - (y - x)
        if coord == "x": paper = {(fold(d[0]), d[1]) for d in paper}
        else:            paper = {(d[0], fold(d[1])) for d in paper}
    return paper

def show(paper):
    for y in range(max(d[1] for d in paper)+1):
        print("".join("#" if (x,y) in paper else " "
            for x in range(max(d[0] for d in paper)+1)))

with open("day13.txt", "r") as fh:
    paper, instructions = read_instructions(fh)
    print("2021 day 13 part 1: %d" % len(fold(paper, instructions[:1])))
    print("2021 day 13 part 2:"); show(fold(paper, instructions))

