def unique_tail_locations(moves, knots):
    rx = [0] * knots
    ry = [0] * knots
    tail_locations = set()
    dirs = {"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0)}
    for move in moves:
        for count in range(int(move[1])):
            rx[0] += dirs[move[0]][0]
            ry[0] += dirs[move[0]][1]
            for i in range(1, knots):
                ox, oy = rx[i-1], ry[i-1]
                if rx[i] == ox and (ry[i] == oy-2 or ry[i] == oy+2):
                    ry[i] += 1 if oy > ry[i] else -1
                elif ry[i] == oy and (rx[i] == ox-2 or rx[i] == ox+2):
                    rx[i] += 1 if ox > rx[i] else -1
                elif (ox > rx[i]+1 or ox < rx[i]-1) or (oy > ry[i]+1 or oy < ry[i]-1):
                    rx[i] += 1 if ox > rx[i] else -1
                    ry[i] += 1 if oy > ry[i] else -1
            tail_locations.add((rx[-1], ry[-1]))
    return len(tail_locations)

with open("day09.txt", "r") as fh:
    moves = [line.split() for line in fh]
    print("2022 day 09 part 1: %d" % unique_tail_locations(moves, 2))
    print("2022 day 09 part 2: %d" % unique_tail_locations(moves, 10))
