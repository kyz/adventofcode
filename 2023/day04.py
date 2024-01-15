def points(matches):
    return 0 if matches == 0 else pow(2, matches - 1)

def count_matches(card):
    parts = card.strip().split()
    mid = parts.index("|")
    return len(set(parts[2:mid]) & set(parts[mid+1:]))

def count_wins(matches):
    count = [1] * len(matches)
    winnings = len(matches)
    for i in range(len(matches)):
        for j in range(i+1, i+1 + matches[i]):
            count[j] += count[i]
            winnings += count[i]
    return winnings

with open("day04.txt", "r") as fh:
    matches = [count_matches(card) for card in fh]
    print("2023 day 04 part 1: %d" % sum(points(m) for m in matches))
    print("2023 day 04 part 2: %d" % count_wins(matches))
