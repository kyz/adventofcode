# https://www.redblobgames.com/grids/hexagons/
move = {
    "n":  lambda pos: (pos[0]+0, pos[1]+1, pos[2]-1),
    "s":  lambda pos: (pos[0]+0, pos[1]-1, pos[2]+1),
    "ne": lambda pos: (pos[0]+1, pos[1]+0, pos[2]-1),
    "nw": lambda pos: (pos[0]-1, pos[1]+1, pos[2]+0),
    "se": lambda pos: (pos[0]+1, pos[1]-1, pos[2]+0),
    "sw": lambda pos: (pos[0]-1, pos[1]+0, pos[2]+1),
}

def distance(pos):
    return max(abs(coord) for coord in pos)

pos, furthest = (0,0,0), 0
with open("day11.txt") as f:
    for dir in f.readline().strip().split(","):
        pos = move[dir](pos)
        furthest = max(furthest, distance(pos))
    print("2017 day 11 part 1: %d" % distance(pos))
    print("2017 day 11 part 2: %d" % furthest)
