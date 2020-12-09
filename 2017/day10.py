from operator import xor
from functools import reduce

class KnotHash(object):
    def __init__(self):
        self.pos = 0
        self.skip = 0
        self.hash = list(range(256))

    def round(self, lengths):
        for l in lengths:
            d, e = self.hash + self.hash, self.pos + l
            d[self.pos:e] = reversed(d[self.pos:e])
            self.hash = d[0:256] if e <= 256 else d[256:e] + d[e-256:-256]
            self.pos = (self.pos + l + self.skip) % 256
            self.skip += 1
        return self

    def update(self, str):
        for i in range(64):
            self.round([ord(c) for c in str] + [17, 31, 73, 47, 23])
        return self

    def digest(self):
        bytes = [reduce(xor, self.hash[i:i+16], 0) for i in range(0, 256, 16)]
        return "".join(["{:02x}".format(b) for b in bytes])

if __name__ == "__main__":
    with open("day10.txt") as f:
        data = f.readline().strip()
        h = KnotHash().round([int(val) for val in data.split(",")]).hash
        print("2017 day 10 part 1: %d" % (h[0] * h[1]))
        print("2017 day 10 part 2: %s" % KnotHash().update(data).digest())
