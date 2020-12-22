import re, functools, operator

def parse_lines(lines):
    rules, i, p = {}, 0, re.compile(r"([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
    while p.match(lines[i]):
        field, lo1, hi1, lo2, hi2 = p.match(lines[i]).groups()
        rules[field] = (int(lo1), int(hi1), int(lo2), int(hi2))
        i += 1
    myticket = [int(x) for x in lines[i+2].split(",")]
    tickets = [[int(x) for x in line.split(",")] for line in lines[i+5:]]
    return rules, myticket, tickets

def invalid_count(rules, ticket):
    total = 0
    for v in ticket:
        valid = False
        for lo1, hi1, lo2, hi2 in rules.values():
            valid |= lo1 <= v <= hi1 or lo2 <= v <= hi2
        if not valid:
            total += v
    return total

def field_columns(rules, tickets):
    num_cols = len(tickets[0])
    col_values = [[t[c] for t in tickets] for c in range(num_cols)]
    col_rules = [{r for r in rules if invalid_count({r: rules[r]}, col_values[c]) == 0}
                 for c in range(num_cols)]
    fields = {}
    while len(fields) < num_cols:
        for col, matching in enumerate(col_rules):
            if len(matching) == 1:
                field = matching.pop()
                fields[field] = col
                for m in col_rules:
                    m.discard(field)
    return fields

def departure_vals(rules, myticket, tickets):
    tickets = [t for t in tickets if invalid_count(rules, t) == 0] # remove invalid
    fields = field_columns(rules, tickets)
    return [myticket[fields[f]] for f in fields if f.startswith("departure")]

with open("day16.txt", "r") as fh:
    rules, myticket, tickets = parse_lines(fh.readlines())
    print("2020 day 16 part 1: %d" % sum(invalid_count(rules, t) for t in tickets))
    print("2020 day 16 part 2: %d" % functools.reduce(operator.mul, departure_vals(rules, myticket, tickets)))
