import intcode

def find_intersections(p):
    rows = "".join([chr(o) for o in intcode.computer(p)]).split("\n")
    w, h = len(rows[0]), len(rows) - 2
    return sum([x*y for x in range(1, w-1) for y in range(1, h-1)
        if rows[y][x] == rows[y][x-1] == rows[y][x+1] ==
           rows[y-1][x] == rows[y+1][x] == '#'])

def walk(p):
    p[0] = 2
    cpu = intcode.computer(p)
    inp = (ord(d) for d in ("A,A,B,C,A,C,B,C,A,B\n" "L,4,L,10,L,6\n"
        "L,6,L,4,R,8,R,8\n" "L,6,R,8,L,10,L,8,L,8\n" "n\n"))
    out = 0
    while out < 128:
        out = next(cpu)
        while out is None:
            out = cpu.send(next(inp))
    return out

with open("day17.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 17 part 1: %d" % find_intersections(p))
    print("2019 day 17 part 2: %d" % walk(p))
