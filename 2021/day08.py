def count_1748_codes(entries):
    return sum(1 if len(code) in {2,3,4,7} else 0 for e in entries for code in e[-4:])

def decode(entry):
    digits = list(sorted((set(s) for s in entry[:10]), key=len))

    # digits we can distinguish by number of segments: 1, 7, 4, 8
    d1, d7, d4, d8 = digits[0], digits[1], digits[2], digits[9]

    # distinguish the 5-segment numbers 2, 3, 5
    d3 = next(d for d in digits[3:6] if d1.issubset(d))
    top_left = d4 - d3
    d2 = next(d for d in digits[3:6] if d != d3 and not top_left.issubset(d))
    d5 = next(d for d in digits[3:6] if d != d2 and d != d3)

    # distinguish the 6-segment numbers 0, 6, 9
    bottom_left = d2 - d3
    mid_bar = d4 - d1 - top_left
    d0 = next(d for d in digits[6:9] if not mid_bar.issubset(d))
    d6 = next(d for d in digits[6:9] if d != d0 and bottom_left.issubset(d))
    d9 = next(d for d in digits[6:9] if d != d0 and d != d6)

    # decode codes
    decoder = {tuple(sorted(s)): str(i)
        for i, s in enumerate([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9])}
    return int("".join(decoder[tuple(sorted(code))] for code in entry[-4:]))

with open("day08.txt", "r") as fh:
    entries = [[s for s in line.split()] for line in fh]
    print("2021 day 08 part 1: %d" % count_1748_codes(entries))
    print("2021 day 08 part 2: %d" % sum(decode(e) for e in entries))
