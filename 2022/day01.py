def top_3_sum(elf_calories):
    return sum(sorted(elf_calories)[-3:])

with open("day01.txt", "r") as fh:
    elf_calories = [sum(int(l) for l in g.split()) for g in fh.read().split("\n\n")]
    print("2022 day 01 part 1: %d" % max(elf_calories))
    print("2022 day 01 part 2: %d" % top_3_sum(elf_calories))
