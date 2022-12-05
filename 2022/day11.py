import functools, operator, re

MONKEY = (r"(Monkey \d+):\n"                           # m[0] = monkey id
          r"  Starting items: ([\d, ]+)\n"             # m[1] = items
          r"  Operation: new = old ([*+]) (\d+|old)\n" # m[2]=op m[3]=operand
          r"  Test: divisible by (\d+)\n"              # m[4] = test
          r"    If true: throw to monkey (\d+)\n"      # m[5] = iftrue
          r"    If false: throw to monkey (\d+)\n")    # m[6] = iffalse

def play_monkeys(monkeys, relief, rounds):
    monkeys = [[0, [int(item) for item in m[1].split(", ")],
        m[2], 0 if m[3] == 'old' else int(m[3]),
        int(m[4]), int(m[5]), int(m[6])] for m in monkeys] # copy and init
    lcm = functools.reduce(operator.mul, (m[4] for m in monkeys))
    for r in range(rounds):
        for m in monkeys:
            for item in m[1]:
                o = m[3] if m[3] != 0 else item
                item = (item * o) if m[2] == '*' else (item + o)
                if relief: item //= 3
                else:      item = item % lcm
                dest = m[5] if (item % m[4]) == 0 else m[6]
                monkeys[dest][1].append(item)
            m[0] += len(m[1]) # number of items inspected
            m[1] = [] # monkey has given away all items
    by_activity = sorted(monkeys, key=lambda m: m[0])
    return by_activity[-1][0] * by_activity[-2][0]

with open("day11.txt", "r") as fh:
    monkeys = [list(m.groups()) for m in re.finditer(MONKEY, fh.read())]
    print("2022 day 11 part 1: %d" % play_monkeys(monkeys, True, 20))
    print("2022 day 11 part 2: %d" % play_monkeys(monkeys, False, 10000))

