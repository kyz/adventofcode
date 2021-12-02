import re

def parse_lines(lines):
    mid = lines.index("")
    rulelist = lines[:mid]
    messages = lines[mid+1:]

    rules = {}
    for r in rulelist:
        i, rule = r.split(": ")
        rules[i] = rule[1] if rule[0] == '"' else rule.split()
    return rules, messages

def to_regexp(rules, i):
    if isinstance(rules[i], str):
        return rules[i]
    else:
        return "(?:" + "".join('|' if r == '|' else to_regexp(rules, r) for r in rules[i]) + ")"

def change_rules(rules):
    a, b = to_regexp(rules, "42"), to_regexp(rules, "31")
    rules["8"] = a + "+"
    rules["11"] = "(?:" + "|".join("%s{%d}%s{%d}" % (a, n, b, n) for n in range(1,5)) + ")"

with open("day19.txt", "r") as fh:
    rules, messages = parse_lines([l.strip() for l in fh.readlines()])
    p1 = re.compile("^" + to_regexp(rules, "0") + "$")
    change_rules(rules)
    p2 = re.compile("^" + to_regexp(rules, "0") + "$")
    print("2020 day 19 part 1: %d" % sum(1 for m in messages if p1.match(m)))
    print("2020 day 19 part 2: %d" % sum(1 for m in messages if p2.match(m)))
