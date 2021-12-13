def parse_line(line):
    openers = {"(", "[", "{", "<"}
    closers = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for c in line:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if not stack or stack[-1] != closers[c]:
                return c
            stack.pop()
    return stack

def sum_error_score(lines):
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return sum(score[l] for l in lines if isinstance(l, str))

def completion_score(stack):
    score = {"(": 1, "[": 2, "{": 3, "<": 4}
    total = 0
    while stack:
        total = total * 5 + score[stack.pop()]
    return total

def mid_completion_score(lines):
    scores = sorted(completion_score(l) for l in lines if isinstance(l, list))
    return scores[len(scores) // 2]

with open("day10.txt", "r") as fh:
    lines = [parse_line(line) for line in fh]
    print("2021 day 10 part 1: %d" % sum_error_score(lines))
    print("2021 day 10 part 2: %d" % mid_completion_score(lines))
