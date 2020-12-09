def do_a_little_dance(dancers, steps):
    d = list(dancers)
    for step in steps:
        if step[0] == "s":
            i = int(step[1:])
            d = d[-i:] + d[0:-i]
        elif step[0] == "x":
            i, j = [int(x) for x in step[1:].split("/")]
            d[i], d[j] = d[j], d[i]
        elif step[0] == "p":
            i, j = d.index(step[1]), d.index(step[3])
            d[i], d[j] = d[j], d[i]
    return "".join(d)

with open("day16.txt") as f:
    data = f.readline().strip().split(",")
    seen = dict()
    seen[0] = "abcdefghijklmnop"
    seen[1] = do_a_little_dance(seen[0], data)
    print("2017 day 16 part 1: %s" % seen[1])
    for i in range(2, 1000):
        seen[i] = do_a_little_dance(seen[i-1], data)
        if seen[i] == seen[0]:
            print("2017 day 16 part 1: %s" % seen[1000000000 % i])
            break
