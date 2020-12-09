def follow_jumps(data, transform):
    ip, steps = 0, 0
    while ip < len(data):
        val = data[ip]
        data[ip] = transform(val)
        ip += val
        steps += 1
    return steps

with open("day05.txt") as f:
    data = [int(line) for line in f]
    inc = lambda x: x + 1
    incto3 = lambda x: x - 1 if x >= 3 else x + 1
    print("2017 day 5 part 1: %d" % follow_jumps(data[:], inc))
    print("2017 day 5 part 2: %d" % follow_jumps(data[:], incto3))
