import re
words = "zero one two three four five six seven eight nine".split(" ")
d = {}
for i, word in enumerate(words): d[word] = d[str(i)] = i
re1 = re.compile(r"([1-9])")
re2 = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))")

def calibrate(val, wordre):
    digits = [d[m.group(1)] for m in re.finditer(wordre, val)]
    return digits[0] * 10 + digits[-1]

with open("day01.txt", "r") as fh:
    vals = fh.readlines()
    print("2023 day 01 part 1: %d" % sum([calibrate(v, re1) for v in vals]))
    print("2023 day 01 part 2: %d" % sum([calibrate(v, re2) for v in vals]))
