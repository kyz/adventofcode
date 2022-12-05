import re

def hits_target(dx, dy, target):
    x, y, max_y = 0, 0, 9
    while x < target[1] and y > target[2]:
        x += dx; dx -= 1 if dx > 0 else 0
        y += dy; dy -= 1
        max_y = max(y, max_y)
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return True, max_y
    return False, max_y

def find_trajectories(target):
    max_y, seen = 0, set()
    for dx in range(1, 300):
        for dy in range(-200, 200):
            hit, my = hits_target(dx, dy, target)
            if hit:
                seen.add((dx, dy))
                max_y = max(max_y, my)
    return max_y, len(seen)

with open("day17.txt", "r") as fh:
    target = [int(n) for n in re.findall(r"-?\d+", fh.readline())]
    max_y, num_seen = find_trajectories(target)
    print("2021 day 17 part 1: %d" % max_y)
    print("2021 day 17 part 2: %d" % num_seen)
