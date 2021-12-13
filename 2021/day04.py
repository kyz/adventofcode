from collections import defaultdict

def bingo(fh):
    parts = [b.strip() for b in fh.read().split("\n\n")]
    nums = [int(n) for n in parts.pop(0).split(",")]
    boards = []
    for p in parts:
        boards.append({(x, y): int(num)
            for x, row in enumerate(p.split("\n"))
            for y, num in enumerate(row.split())})

    marked, won, scores = set(), set(), list()
    for n in nums:
        marked.add(n)
        for i, board in enumerate(boards):
            if i not in won:
                for x in range(5):
                    h = sum(1 if board[x, y] in marked else 0 for y in range(5))
                    v = sum(1 if board[y, x] in marked else 0 for y in range(5))
                    if h == 5 or v == 5:
                        won.add(i)
                        scores.append(n * sum(set(board.values()) - marked))
    return scores[0], scores[-1]

with open("day04.txt", "r") as fh:
    first, last = bingo(fh)
    print("2021 day 04 part 1: %d" % first)
    print("2021 day 04 part 2: %d" % last)
