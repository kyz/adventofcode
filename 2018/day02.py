from collections import Counter

def count_2s_3s(ids):
    twos, threes = 0, 0
    for id in ids:
        c = Counter(id).most_common()
        if [1 for x in c if x[1] == 2]: twos += 1
        if [1 for x in c if x[1] == 3]: threes += 1
    return twos * threes

def differ_by_1_char(ids):
    ids = sorted(ids)
    for i in range(len(ids) - 1):
        id1, id2 = ids[i], ids[i+1]
        if sum(1 for j in range(len(id1)) if id1[j] != id2[j]) == 1:
            return "".join(id1[j] for j in range(len(id1)) if id1[j] == id2[j])

with open("day02.txt", "r") as fh:
    ids = [line.strip() for line in fh]
    print("2018 day 02 part 1: %d" % count_2s_3s(ids))
    print("2018 day 02 part 2: %s" % differ_by_1_char(ids))
