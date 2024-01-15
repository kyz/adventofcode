import functools, math, operator

# winning is when x*(t-x) > d for 0<x<t
# we can find when winning starts then stops
# as the roots of x*(t-x)-d=0
def wins(td):
    t, d = td
    root1 = int((-t + math.sqrt(t*t - 4*d)) / -2)
    root2 = int((-t - math.sqrt(t*t - 4*d)) / -2)
    return root2 - root1

def mul_wins(td):
    return functools.reduce(operator.mul, map(wins, td))

with open("day06.txt", "r") as fh:
    times = fh.readline().split(":")[1].strip().split()
    dists = fh.readline().split(":")[1].strip().split()
    td1 = list(zip(map(int, times), map(int, dists)))
    td2 = list(map(int, ["".join(times), "".join(dists)]))
    print("2023 day 06 part 1: %d" % mul_wins(td1))
    print("2023 day 06 part 2: %d" % wins(td2))
