import re

def parse_valves(data):
    flows, dests = {}, {}
    for m in re.finditer(r"Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", data):
        dests[m.group(1)] = set(m.group(3).split(", "))
        if int(m.group(2)) > 0: flows[m.group(1)] = int(m.group(2)) # non-zero flows only
    return flows, dests

def all_costs(nodes): # cost[a,b] = time needed to move from a to b and open a valve
    def dist(a, b):
        cur = {a}
        for dist in range(len(dests)):
            if b in cur: return dist
            cur = set().union(*(dests[c] for c in cur))
    return {(a,b): dist(a,b) + 1 for a in nodes for b in nodes}

def open_all_valves(best_flow, time_left, cur_pos="AA", cur_flow=0, opened=0):
    if cur_flow > best_flow.get(opened, 0):
        best_flow[opened] = cur_flow # highest flow for this combo of open valves
    for vi, vn in valves:
        t = time_left - costs[cur_pos, vn] # if we have time to open this valve,
        if t > 0 and (opened & vi) == 0: # and we haven't opened this valve before...
            open_all_valves(best_flow, t, vn, cur_flow + flows[vn] * t, opened | vi)
    return best_flow

def best_single_path(): # highest-flow single path
    return max(open_all_valves({}, 30).values())

def best_twin_path(): # highest-flow pair of paths that don't open each other's valves
    best = open_all_valves({}, 26)
    return max(best[u] + best[e] for u in best for e in best if (u & e) == 0)

with open("day16.txt", "r") as fh:
    flows, dests = parse_valves(fh.read())
    costs = all_costs({"AA"} | set(flows))
    valves = [(1 << i, vn) for i, vn in enumerate(flows)]
    print("2022 day 16 part 1: %d" % best_single_path())
    print("2022 day 16 part 2: %d" % best_twin_path())
