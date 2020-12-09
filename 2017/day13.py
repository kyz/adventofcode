def hits(data, delay):
    return [x for x in data if (x + delay) % (data[x] * 2 - 2) == 0]

with open("day13.txt") as f:
    data = {int(line.split(":")[0]) : int(line.split(":")[1]) for line in f}
    severity = sum([x * data[x] for x in hits(data, 0)])
    print("2017 day 13 part 1: %d" % severity)
    for delay in range(5000000):
        if len(hits(data, delay)) == 0:
            print("2017 day 13 part 2: %d" % delay)
            break
