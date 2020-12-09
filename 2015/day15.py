import re

def get_recipes(lines):
    return [[int(g) for g in re.findall(r"-?\d+", line)] for line in lines]

def best_mix(r):
    best_full, best_500 = 0, 0
    for i in range(101):
        for j in range(101-i):
            for k in range(101-(i+j)):
                for l in range(101-(i+j+k)):
                    if i+j+k+l == 100:
                        c = r[0][0]*i + r[1][0]*j + r[2][0]*k + r[3][0]*l
                        d = r[0][1]*i + r[1][1]*j + r[2][1]*k + r[3][1]*l
                        f = r[0][2]*i + r[1][2]*j + r[2][2]*k + r[3][2]*l
                        t = r[0][3]*i + r[1][3]*j + r[2][3]*k + r[3][3]*l
                        x = r[0][4]*i + r[1][4]*j + r[2][4]*k + r[3][4]*l
                        if c > 0 and d > 0 and f > 0 and t > 0:
                            score = c * d * f * t
                            best_full = max([best_full, score])
                            if x == 500: best_500 = max([best_500, score])
    return (best_full, best_500)

with open("day15.txt") as fh:
    best = best_mix(get_recipes(fh.readlines()))
    print("2015 day 15 part 1: %d" % best[0])
    print("2015 day 15 part 2: %d" % best[1])
