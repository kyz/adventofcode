import re, collections

def count_valid(passwords, valid):
    count = 0
    m = re.compile(r"(\d+)-(\d+) (.): (.+)")
    for p in passwords:
        n1, n2, c, password = m.match(p).groups()
        if valid(int(n1), int(n2), c, password):
            count += 1
    return count

def policy1(lo, hi, c, password):
    letterfreq = collections.Counter(password)
    return lo <= letterfreq[c] <= hi

def policy2(p1, p2, c, password):
    return (password[p1-1] == c) ^ (password[p2-1] == c)

with open("day02.txt", "r") as fh:
    passwords = [line.strip() for line in fh.readlines()]
    print("2020 day 02 part 1: %d" % count_valid(passwords, policy1))
    print("2020 day 02 part 2: %d" % count_valid(passwords, policy2))
