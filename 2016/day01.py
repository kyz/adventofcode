def move_distance(moves, stop_at_revisit):
    x, y, angle, seen = 0, 0, 0, set()
    move_x, move_y = [0,1,0,-1], [-1,0,1,0]
    for m in moves:
        angle += 1 if m[0] == "R" else -1
        for d in range(int(m[1:])):
            x += move_x[angle % 4]
            y += move_y[angle % 4]
            if stop_at_revisit and (x,y) in seen:
                return abs(x) + abs(y)
            seen.add((x,y))
    return abs(x) + abs(y)

with open("day01.txt", "r") as fh:
    moves = fh.readline().split(", ")
    print("2016 day 01 part 1: %d" % move_distance(moves, False))
    print("2016 day 01 part 2: %d" % move_distance(moves, True))
