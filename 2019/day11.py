import intcode
from collections import defaultdict

def paint(p, initial):
    cpu = intcode.computer(p)
    next(cpu)
    panel = defaultdict(int)
    x, y, facing = 0, 0, 0
    moves = [(0,-1), (1,0), (0,1), (-1,0)]
    panel[x,y] = initial
    while True:
        panel[x,y] = cpu.send(panel[x,y])
        facing = (facing + 1 if next(cpu) else facing - 1) % len(moves)
        x += moves[facing][0]
        y += moves[facing][1]
        try: next(cpu)
        except StopIteration: return panel

def render(panel):
    w = max([k[0] for k in panel]) + 1
    h = max([k[1] for k in panel]) + 1
    for y in range(h):
        print("".join(['#' if panel[x,y] else ' ' for x in range(w)]))

with open("day11.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 11 part 1: %d" % len(paint(p, 0).keys()))
    render(paint(p, 1))
