import re

def parse_rules(rules):
    return {bag: {b: int(n) for (n, b) in re.findall("(\d+) (.+?) bags?", contents)}
        for (bag, contents) in [re.match(r"^(.+) bags contain (.+)\.$", r).groups()
        for r in rules]}

def count_holders(rules, what):
    def can_hold(b):
        if what in rules[b]: return True
        for bb in rules[b]:
            if can_hold(bb): return True
    return len([1 for bag in rules if can_hold(bag)])

def bags_inside(rules, bag):
    if rules[bag]:
        return sum([(1 + bags_inside(rules, b)) * n for (b,n) in rules[bag].items()])
    else:
        return 0

with open("day07.txt", "r") as fh:
    rules = parse_rules(fh.readlines())
    print("2020 day 07 part 1: %d" % count_holders(rules, "shiny gold"))
    print("2020 day 07 part 2: %d" % bags_inside(rules, "shiny gold"))
