cancel_next, in_garbage = False, False
nesting, score, garbage = 0, 0, 0
with open("day09.txt") as f:
    for c in f.readline():
        if cancel_next:
            cancel_next = False
        elif c == "!":
            cancel_next = True
        elif c == "<" and not in_garbage:
            in_garbage = True
        elif c == ">" and in_garbage:
            in_garbage = False
        elif c == "{" and not in_garbage:
            nesting += 1
        elif c == "}" and not in_garbage:
            score += nesting
            nesting -= 1
        elif in_garbage:
            garbage += 1
    print("2017 day 9 part 1: %d" % score)
    print("2017 day 9 part 2: %d" % garbage)
