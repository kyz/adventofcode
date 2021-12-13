def lanternfish(existing_ages, days):
    aged = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in existing_ages:
        aged[a] += 1

    for d in range(days):
        spawning = aged[0]
        for i in range(8):
            aged[i] = aged[i+1]
        aged[6] += spawning
        aged[8] = spawning
    return sum(aged)

with open("day06.txt", "r") as fh:
    ages = [int(n) for n in fh.readline().split(",")]
    print("2021 day 06 part 1: %d" % lanternfish(ages, 80))
    print("2021 day 06 part 1: %d" % lanternfish(ages, 256))
386536
