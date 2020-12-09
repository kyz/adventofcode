count, floor, been_to_basement = 0, 0, False
with open("day01.txt") as fh:
    for c in fh.readline():
        floor += 1 if c == "(" else -1
        count += 1
        if floor == -1 and not been_to_basement:
            print("2015 day 1 part 2: %d" % count)
            been_to_basement = True
    print("2015 day 1 part 1: %d" % floor)
