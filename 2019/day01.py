def fuel_required(mass):
    return (mass // 3) - 2 if mass > 8 else 0

def total_required(mass):
    total = 0
    while mass > 0:
        mass = fuel_required(mass)
        total += mass
    return total

with open("day01.txt") as fh:
    masses = [int(m) for m in fh.readlines()]
    print("2019 day 1 part 1: %d" % sum([fuel_required(m) for m in masses]))
    print("2019 day 1 part 2: %d" % sum([total_required(m) for m in masses]))
