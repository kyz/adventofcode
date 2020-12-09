from itertools import permutations

def distance(itinery):
    travelled, prev = 0, itinery[0]
    for city in itinery[1:]:
        travelled += distances[(prev, city)]
        prev = city
    return travelled

cities, distances = set(), dict()
with open("day09.txt") as fh:
    for line in fh:
        city1, to_, city2, eq_, dist = line.split()
        cities.add(city1)
        cities.add(city2)
        distances[(city1, city2)] = distances[(city2, city1)] = int(dist)

    all_runs = [distance(x) for x in permutations(cities)]
    print("2015 day 9 part 1: %d" % min(all_runs))
    print("2015 day 9 part 2: %d" % max(all_runs))
