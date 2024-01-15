import collections, itertools

type_ranks = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)]
card_ranks = "23456789TJQKA"
joker_ranks = "J23456789TQKA"

def type_rank(hand):
    return type_ranks.index(tuple(sorted(collections.Counter(hand).values())))

def normal_rank(hand):
    return type_rank(hand), tuple(card_ranks.index(h) for h in hand)

def joker_rank(hand):
    non_jokers = hand.replace("J", "")
    jlen = len(hand) - len(non_jokers)
    max_rank = 6 if jlen == 5 else max(type_rank(non_jokers + "".join(j))
        for j in itertools.product(non_jokers, repeat=jlen))
    return (max_rank, tuple(joker_ranks.index(h) for h in hand))

def winnings(hand_bids, ranker):
    score = lambda hb: (hb[0]+1) * hb[1][1]
    rank = lambda hb: ranker(hb[0])
    return sum(map(score, enumerate(sorted(hand_bids, key=rank))))

with open("day07.txt", "r") as fh:
    hand_bids = [(line.split()[0], int(line.split()[1])) for line in fh]
    print("2023 day 07 part 1: %d" % winnings(hand_bids, normal_rank))
    print("2023 day 07 part 2: %d" % winnings(hand_bids, joker_rank))
