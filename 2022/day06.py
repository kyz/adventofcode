def find_unique_sequence(s, l):
    for x in range(len(s)-l):
        if len(set(s[x:x+l])) == l:
            return x+l

with open("day06.txt", "r") as fh:
    code = fh.readline().strip()
    print("2022 day 06 part 1: %d" % find_unique_sequence(code, 4))
    print("2022 day 06 part 2: %d" % find_unique_sequence(code, 14))

