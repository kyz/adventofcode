import re

def unescape(s):
    return re.sub(r"\\(?:x[0-9a-f]{2}|.)", ".", s[1:-1])
def escape(s):
    return '"' + s.replace("\\", "\\\\").replace("\"", "\\\"") + '"'

with open("day08.txt") as fh:
    data = [line.strip() for line in fh]
    diff_unescaped = sum([len(line) - len(unescape(line)) for line in data])
    diff_escaped = sum([len(escape(line)) - len(line) for line in data])
    print("2015 day 8 part 1: %d" % diff_unescaped)
    print("2015 day 8 part 2: %d" % diff_escaped)
