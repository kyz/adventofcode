import intcode

walls = dict()

def map_area(p, pos):
    cpu = intcode.computer(p); next(cpu)
    def traverse(pos):
        for i, move in enumerate(nesw(pos)):
            if move not in walls:
                walls[move] = cpu.send([1,4,2,3][i]); next(cpu)
                if walls[move]:
                    traverse(move)
                    cpu.send([2,3,1,4][i]); next(cpu) # backtrack
    traverse(pos)

def shortest_path(path):
    paths = []
    for move in nesw(path[-1]):
        if walls[move] == 2: return path + [move]
        if walls[move] == 1 and move not in path:
            best = shortest_path(path + [move])
            if best is not None: paths.append(best)
    return min(paths, key=len) if paths else None

def flood(pos):
    walls[pos] = 0
    moves = [flood(move) + 1 for move in nesw(pos) if walls[move]]
    return max(moves) if moves else 0

def nesw(p):
    return [(p[0], p[1]-1), (p[0]+1, p[1]), (p[0], p[1]+1), (p[0]-1, p[1])]
    
with open("day15.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    c = (100, 100)
    map_area(p, c)
    path = shortest_path([c])
    print("2019 day 15 part 1: %d" % (len(path) - 1))
    print("2019 day 15 part 2: %d" % flood(path[-1]))
