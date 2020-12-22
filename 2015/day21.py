def outfits():
    none = (0,0,0)
    swords = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
    armour = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
    rings  = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
    for s in swords:
        for a in [none] + armour:
            for r1 in [none] + rings:
                for r2 in [none] + rings:
                    if r1 != r2 or r2 == none:
                        yield (s[0] + a[0] + r1[0] + r2[0],
                               s[1] + a[1] + r1[1] + r2[1],
                               s[2] + a[2] + r1[2] + r2[2])

def win_fight(stats, boss_stats):
    hp, dmg, arm = stats
    boss_hp, boss_dmg, boss_arm = boss_stats
    while hp > 0:
        boss_hp -= max([1, dmg - boss_arm])
        if boss_hp <= 0: return True
        hp -= max([1, boss_dmg - arm])
    return False

def cheapest_win(boss_stats):
    return min((o[0] for o in outfits()
        if win_fight((100, o[1], o[2]), boss_stats)))

def most_expensive_loss(boss_stats):
    return max((o[0] for o in outfits()
        if not win_fight((100, o[1], o[2]), boss_stats)))

with open("day21.txt", "r") as fh:
    boss_stats = tuple([int(line.split()[-1]) for line in fh.readlines()])
    print("2015 day 21 part 1: %d" % cheapest_win(boss_stats))
    print("2015 day 21 part 2: %d" % most_expensive_loss(boss_stats))
