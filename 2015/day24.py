import functools, itertools, operator

def balance(weights, compartments):
    target_weight = sum(weights) // compartments
    for n in range(len(weights)):
        for x in itertools.combinations(weights, n):
            if sum(x) == target_weight:
                return functools.reduce(operator.mul, x)

with open("day24.txt", "r") as fh:
    weights = [int(line) for line in fh]
    print("2015 day 24 part 1: %d" % balance(weights, 3))
    print("2015 day 24 part 2: %d" % balance(weights, 4))

