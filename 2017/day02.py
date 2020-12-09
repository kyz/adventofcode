from itertools import permutations

with open("day02.txt") as f:
    data = [[int(val) for val in line.split()] for line in f]
    biggest_diff = sum([max(row) - min(row) for row in data])
    even_divisions = sum([[int(x[0] / x[1]) for x in permutations(row, 2)
                           if x[0] % x[1] == 0][0] for row in data])
    print("2017 day 2 part 1: %d" % biggest_diff)
    print("2017 day 2 part 2: %d" % even_divisions)
