first_decode = {"X": "A", "Y": "B", "Z": "C"}
second_decode = {
   ("A", "X"): "C", ("B", "X"): "A", ("C", "X"): "B", # lose
   ("A", "Y"): "A", ("B", "Y"): "B", ("C", "Y"): "C", # draw
   ("A", "Z"): "B", ("B", "Z"): "C", ("C", "Z"): "A", # win
}
value = {"A": 1, "B": 2, "C": 3}
wins = {("A", "C"), ("B", "A"), ("C", "B")}

def score(a, b):
    return value[a] + (3 if a == b else 6 if (a, b) in wins else 0)

def strat_score(strats):
    return sum(score(first_decode[s[1]], s[0]) for s in strats)

def real_strat_score(strats):
    return sum(score(second_decode[s[0], s[1]], s[0]) for s in strats)

with open("day02.txt", "r") as fh:
    strats = [l.split() for l in fh.readlines()]
    print("2022 day 02 part 1: %d" % strat_score(strats))
    print("2022 day 02 part 2: %d" % real_strat_score(strats))

