def lowest_fuel(posns, fuel_calc):
    return min(sum(fuel_calc(src, dest) for src in posns)
        for dest in range(min(posns), max(posns)+1))

def linear_burn(src, dest):
    return abs(src - dest)

def triangle_burn(src, dest):
    n = abs(src - dest)
    return (n * (n + 1)) // 2

with open("day07.txt", "r") as fh:
    posns = [int(n) for n in fh.readline().split(",")]
    print("2021 day 07 part 1: %d" % lowest_fuel(posns, linear_burn))
    print("2021 day 07 part 2: %d" % lowest_fuel(posns, triangle_burn))

