def priorities(items):
    return sum(1  + ord(i) - ord('a') if i >= 'a' and i <= 'z' else
               27 + ord(i) - ord('A') for i in items)

def common_per_half_sack(sacks):
    return priorities(list(set(s[:len(s)//2]) &
                           set(s[len(s)//2:]))[0] for s in sacks)

def common_per_sack_trio(sacks):
    return priorities(list(set(s[0]) & set(s[1]) & set(s[2]))[0]
        for s in zip(*([iter(sacks)] * 3)))

with open("day03.txt", "r") as fh:
    sacks = [l.strip() for l in fh.readlines()]
    print("2022 day 03 part 1: %d" % common_per_half_sack(sacks))
    print("2022 day 03 part 2: %d" % common_per_sack_trio(sacks))

