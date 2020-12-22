cardinal = {"E":(1,0), "S":(0,1), "W":(-1,0), "N":(0,-1)}
rot = {('R',90): 1, ('R',180): 2, ('R',270): 3,
       ('L',90): 3, ('L',180): 2, ('L',270): 1}

def distance(instructions, wx, wy, part2):
    x, y = 0, 0
    for (i, n) in instructions:
        if i == 'L' or i == 'R':
            for c in range(rot[i,n]):
                wx, wy = -wy, wx
        elif i == 'F':
            x += wx * n
            y += wy * n
        elif part2:
            wx += cardinal[i][0] * n
            wy += cardinal[i][1] * n
        else:
            x += cardinal[i][0] * n
            y += cardinal[i][1] * n
    return abs(x) + abs(y)

with open("day12.txt", "r") as fh:
    instructions = [(line[0], int(line[1:])) for line in fh.readlines()]
    print("2020 day 12 part 1: %d" % distance(instructions, 1, 0, False))
    print("2020 day 12 part 2: %d" % distance(instructions, 10, -1, True))


