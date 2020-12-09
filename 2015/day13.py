import re
from itertools import permutations
from collections import defaultdict

def read_list(fh):
    re1 = re.compile(r"(\S+) would (gain|lose) (\d+) happiness units by sitting next to (\S+)\.")
    happy, people = defaultdict(int), set()
    for line in fh:
        a, gainlose, amount, b = re1.match(line).groups()
        happy[(a,b)] = int(amount) * (-1 if gainlose == "lose" else 1)
        people.add(a)
        people.add(b)
    return happy, people

def happiness(happy, people):
    return sum([happy[(people[i-1], people[i])] +
                happy[(people[i],   people[i-1])] for i in range(len(people))])

def max_happy(happy, people):
    return max([happiness(happy, p) for p in permutations(people)])

with open("day13.txt") as fh:
    happy, people = read_list(fh)
    print("2015 day 13 part 1: %d" % max_happy(happy, people))
    people.add("ME!")
    print("2015 day 13 part 2: %d" % max_happy(happy, people))
