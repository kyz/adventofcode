def paired_digits_count(data, skip):
    return sum([int(d) for i, d in enumerate(data) if data[i - skip] == d])

with open("day01.txt") as f:
    data = f.readline()
    half = int(len(data) / 2)
    print("2017 day 1 part 1: %d" % paired_digits_count(data, 1))
    print("2017 day 1 part 2: %d" % paired_digits_count(data, half))
