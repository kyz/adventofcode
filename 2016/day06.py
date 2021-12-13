import collections

def error_corrected(words, idx):
    return "".join(collections.Counter(w[i] for w in words).most_common()[idx][0]
        for i in range(len(words[0])))

with open("day06.txt", "r") as fh:
    words = [line.strip() for line in fh]
    print("2016 day 06 part 1: %s" % error_corrected(words, 0))
    print("2016 day 06 part 1: %s" % error_corrected(words, -1))

