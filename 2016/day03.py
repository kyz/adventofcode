def possible_triangles(triangles):
    possible = lambda a,b,c: (a+b > c) and (b+c > a) and (c+a > b)
    return sum(1 if possible(*t) else 0 for t in triangles)

def rotate(t):
    out = []
    for y in range(0, len(t), 3):
        for x in range(3):
            out.append([t[y][x], t[y+1][x], t[y+2][x]])
    return out

with open("day03.txt", "r") as fh:
    triangles = [[int(n) for n in line.split()] for line in fh]
    rotated = rotate(triangles)
    print("2016 day 03 part 1: %d" % possible_triangles(triangles))
    print("2016 day 03 part 2: %d" % possible_triangles(rotated))
