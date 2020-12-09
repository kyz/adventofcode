from collections import Counter

data = "3113322113"

def lookandsay(s):
    out, cur, cnt = "", "", 0
    for c in s:
        if c == cur:
            cnt += 1
        else:
            if cnt > 0:
                out += str(cnt) + cur
            cur, cnt = c, 1
    if cnt > 0:
        out += str(cnt) + cur
    return out

for x in range(40):
    data = lookandsay(data)
print("2015 day 10 part 1: %d" % len(data))

for x in range(10):
    data = lookandsay(data)
print("2015 day 10 part 2: %d" % len(data))
