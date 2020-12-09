import re

def part1(words):
    re1 = re.compile(r'(?:[aeiou].*){3}')
    re2 = re.compile(r'([a-z])\1')
    re3 = re.compile(r'(?:ab|cd|pq|xy)')
    return len([w for w in words
        if re1.search(w) and re2.search(w) and not re3.search(w)])

def part2(words):
    re1 = re.compile(r'([a-z]{2}).*\1') 
    re2 = re.compile(r'([a-z]).\1')
    return len([w for w in words
        if re1.search(w) and re2.search(w)])

with open("day05.txt") as fh:
    words = fh.readlines()
    print("2015 day 5 part 1: %d" % part1(words))
    print("2015 day 5 part 2: %d" % part2(words))
