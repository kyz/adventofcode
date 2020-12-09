from collections import Counter

def grouping(l, size):
    return [l[i:i+size] for i in range(0, len(l), size)]

def checksum(layers):
    c = sorted([Counter(l) for l in layers], key=lambda x: x['0'])
    return c[0]['1'] * c[0]['2']

def flatten(layers):
    return [pixel(p) for p in zip(*layers)]

def pixel(pixels):
    for p in pixels:
        if p == '0': return ' '
        if p == '1': return '#'
    return '#'

with open("day08.txt") as fh:
    w, h = 25, 6
    layers = grouping(fh.read().strip(), w * h)
    print("2019 day 8 part 1: %d" % checksum(layers))
    for row in grouping(flatten(layers), w):
        print("".join(row))
