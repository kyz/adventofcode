def diffs(vals):
    out = [vals]
    while not all(v == 0 for v in out[-1]):
        out.append([out[-1][i] - out[-1][i-1] for i in range(1, len(out[-1]))])
    return reversed(out)

def predict_next(vals):
    return sum(v[-1] for v in diffs(vals))

def predict_prev(vals):
    c = 0
    for i in diffs(vals):
        c = i[0] - c
    return c

with open("day09.txt", "r") as fh:
    data = [[int(x) for x in line.split()] for line in fh]
    print("2023 day 09 part 1: %d" % sum(predict_next(x) for x in data))
    print("2023 day 09 part 2: %d" % sum(predict_prev(x) for x in data))
