from functools import cmp_to_key
import json

def read_packets(data):
    return [json.loads(line) for line in data if line != "\n"]

def cmp(l, r):
    if type(l) == int and type(r) == int:
        return l - r
    if type(l) == int: l = (l,)
    if type(r) == int: r = (r,)
    for i in range(min([len(l), len(r)])):
        c = cmp(l[i], r[i])
        if c != 0: return c
    return len(l) - len(r)

def sum_valid_packet_pairs(packets):
    return sum((i // 2) + 1 for i in range(0, len(packets), 2)
        if cmp(packets[i], packets[i+1]) < 0)

def find_divider_packets(packets):
    div1, div2 = [[2]], [[6]]
    p = sorted(packets + [div1, div2], key=cmp_to_key(cmp))
    return (p.index(div1)+1) * (p.index(div2)+1)

with open("day13.txt", "r") as fh:
    packets = read_packets(fh.readlines())
    print("2022 day 13 part 1: %d" % sum_valid_packet_pairs(packets))
    print("2022 day 13 part 2: %d" % find_divider_packets(packets))
