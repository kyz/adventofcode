import math, queue

def lowest_risk(rmap):
    w, h = max(k[0] for k in rmap), max(k[1] for k in rmap)

    start = (0,0)
    goal = (w, h)
    heuristic = lambda a, b : abs(b[0] - a[0]) + abs(b[1] - a[1])
    neighbours = lambda x, y : [k for k in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if k in rmap]

    frontier = queue.PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = frontier.get()
        if current == goal:
            break

        for n in neighbours(*current):
            new_cost = cost_so_far[current] + rmap[n]
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                came_from[n] = current
                cost_so_far[n] = new_cost
                frontier.put(n, new_cost + heuristic(n, goal))

    return cost_so_far[goal]

def expand(rmap):
    w, h = max(k[0] for k in rmap)+1, max(k[1] for k in rmap)+1
    mod9 = lambda n: n - 9 if n > 9 else n
    for y in range(h * 5):
        for x in range(w * 5):
            if x >= w or y >= h:
                rmap[x, y] = mod9(rmap[x % w, y % h] + x // w + y // h)
    return rmap

with open("day15.txt", "r") as fh:
    rmap = {(x,y): int(c) for y, line in enumerate(fh) for x, c in enumerate(line.strip())}
    print("2021 day 15 part 1: %d" % lowest_risk(rmap))
    print("2021 day 15 part 2: %d" % lowest_risk(expand(rmap)))
