class State:
    def __init__(self, hp, m, bhp, bd, hm, ms=0, s=0, p=0, r=0):
        self.hp, self.mana, self.boss_hp, self.boss_dmg, self.hard_mode = hp, m, bhp, bd, hm
        self.mana_spent, self.shield, self.poison, self.recharge = ms, s, p, r
    def copy(self):
        return State(self.hp, self.mana, self.boss_hp, self.boss_dmg, self.hard_mode,
            self.mana_spent, self.shield, self.poison, self.recharge)

def apply_effects(s):
    if s.shield:
        s.shield -= 1
    if s.poison:
        s.poison -= 1
        s.boss_hp -= 3
    if s.recharge:
        s.recharge -= 1
        s.mana += 101

def magic_missile(s): s.boss_hp -= 4
def drain(s):         s.boss_hp -= 2; s.hp += 2
def shield(s):        s.shield = 6
def poison(s):        s.poison = 6
def recharge(s):      s.recharge = 5

spells = [
    (magic_missile, 53, lambda s: s.mana >= 53),
    (drain,         73, lambda s: s.mana >= 73),
    (shield,       113, lambda s: s.mana >= 113 and s.shield == 0),
    (poison,       173, lambda s: s.mana >= 173 and s.poison == 0),
    (recharge,     229, lambda s: s.mana >= 229 and s.recharge == 0),
]

def take_turn(s, spell):
    # your turn
    if s.hard_mode:
        s.hp -= 1
        if s.hp <= 0: return s # we died
    s.mana -= spell[1]
    s.mana_spent += spell[1]
    spell[0](s)

    # boss's turn
    armour = 7 if s.shield > 0 else 0
    apply_effects(s)
    if s.boss_hp > 0:
        s.hp -= max([1, s.boss_dmg - armour])

    apply_effects(s) # apply effects in advance of player turn
    return s

FAIL = 999999999 # higher than any normal score

def lowest_win(s):
    global lowest_win_so_far

    if s.boss_hp <= 0:
        if s.mana_spent < lowest_win_so_far:
            lowest_win_so_far = s.mana_spent
        return s.mana_spent # we won!

    if s.hp <= 0 or s.mana < 53 or s.mana_spent >= lowest_win_so_far:
        return FAIL

    return min((lowest_win(take_turn(s.copy(), sp)) for sp in spells if sp[2](s)))

def lowest_mana_win(boss_stats, hard_mode):
    global lowest_win_so_far
    lowest_win_so_far = FAIL
    s = State(50, 500, boss_stats[0], boss_stats[1], hard_mode)
    return lowest_win(s)

with open("day22.txt", "r") as fh:
    boss_stats = [int(line.split()[-1]) for line in fh.readlines()]
    print("2015 day 22 part 1: %d" % lowest_mana_win(boss_stats, False))
    print("2015 day 22 part 2: %d" % lowest_mana_win(boss_stats, True))
