import collections, itertools, re

def mask_values(program, part2):
    mem = collections.defaultdict(int)
    for p in program:
        m = re.match(r"mask = ([01X]{36})", p)
        if m:
            mask = m.group(1)
            or_mask = int(mask.replace("X", "0"), 2)
            and_mask = int(mask.replace("X", "1"), 2)
        else:
            m = re.match(r"mem\[(\d+)\] = (\d+)", p)
            if m:
                addr, val = m.groups()
                if part2:
                    addr = "{0:036b}".format(int(addr))
                    bits = ["01" if m == "X" else "1" if m == "1" else a
                            for a, m in zip(addr, mask)]
                    for a in itertools.product(*bits):
                        mem[int("".join(a), 2)] = int(val)
                else:
                    mem[addr] = (int(val) | or_mask) & and_mask
    return sum(mem.values())

with open("day14.txt", "r") as fh:
    program = [line.strip() for line in fh.readlines()]
    print("2020 day 14 part 1: %d" % mask_values(program, False))
    print("2020 day 14 part 2: %d" % mask_values(program, True))

