from collections import defaultdict

def parse_recipes(recipes):
    out = dict()
    ingred = lambda x: (int(x.split(" ")[0]), x.split(" ")[1])
    for r in recipes:
        i, o = r.strip().split(" => ")
        o = ingred(o)
        out[o[1]] = [o] + [ingred(i) for i in i.split(", ")]
    return out

def ore_needed(recipes, fuel_wanted=1):
    reserves = defaultdict(int)
    consumed = defaultdict(int)
    reserves['ORE'] = 1000000000000
    need('FUEL', fuel_wanted, recipes, reserves, consumed)
    return consumed['ORE']

def need(ingred, qty, recipes, reserves, consumed):
    if reserves[ingred] < qty:
        recipe = recipes[ingred]
        produces = recipe[0][0]
        batches = ((qty - reserves[ingred]) + (produces-1)) // produces
        for i in recipe[1:]:
            need(i[1], i[0] * batches, recipes, reserves, consumed)
        reserves[ingred] += produces * batches
    reserves[ingred] -= qty
    consumed[ingred] += qty

def max_fuel(recipes):
    fuel, step = 1, 2 ** 20
    while step > 0:
        try:
            ore_needed(recipes, fuel)
            fuel += step
        except KeyError: # ran out of ORE, try again in smaller steps
            fuel -= step
            step //= 2
    return fuel

with open("day14.txt") as fh:
    recipes = parse_recipes(fh.readlines())
    print("2019 day 14 part 1: %d" % ore_needed(recipes))
    print("2019 day 14 part 2: %d" % max_fuel(recipes))
