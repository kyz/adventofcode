def decode(s):
   return int(s.replace('F', '0').replace('B', '1')
               .replace('L', '0').replace('R', '1'), 2)

def myseat(seats):
    allseats = set(range(min(seats), max(seats)))
    return list(allseats.difference(seats))[0]

with open("day05.txt", "r") as fh:
    passes = [line.strip() for line in fh.readlines()]
    seats = [decode(p) for p in passes]
    print("2020 day 05 part 1: %d" % max(seats))
    print("2020 day 05 part 2: %d" % myseat(seats))

