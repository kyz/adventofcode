def matches(start, end):
    c1, c2 = 0, 0
    for x in range(start, end + 1):
        d1, d2, d3, d4, d5, d6 = list(str(x))
        if d2 >= d1 and d3 >= d2 and d4 >= d3 and d5 >= d4 and d6 >= d5:
            if d1 == d2 or d2 == d3 or d3 == d4 or d4 == d5 or d5 == d6:
                c1 += 1
                if ((d1 == d2 and d2 != d3)              or
                    (d2 == d3 and d3 != d4 and d2 != d1) or
                    (d3 == d4 and d4 != d5 and d3 != d2) or
                    (d4 == d5 and d5 != d6 and d4 != d3) or
                    (d5 == d6 and              d5 != d4)):
                    c2 += 1
    return c1, c2

results = matches(307237, 769058)
print("2019 day 3 part 1: %d" % results[0])
print("2019 day 3 part 2: %d" % results[1])
