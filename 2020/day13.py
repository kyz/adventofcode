from gcd import lcm

def firstbus(time, ids):
    for t in range(time, time + 10000):
        for o, p in ids:
            if (t % p) == 0: return p * (t - time)

def earliest(ids):
    time, interval = ids[0]
    for offset, period in ids[1:]:
        while True:
            if (time + offset) % period == 0:
                break
            time += interval
        interval = lcm(interval, period)
    return time

with open("day13.txt", "r") as fh:
    time = int(fh.readline())
    ids = [(o, int(p)) for o,p in enumerate(fh.readline().split(",")) if p != 'x']
    print("2020 day 13 part 1: %d" % firstbus(time, ids))
    print("2020 day 13 part 2: %d" % earliest(ids))
